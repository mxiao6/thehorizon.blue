import graphene
from database import db_session
from models import Post, Tag, Category
from .objectTypes import User
from .utils import decode

# for visibility
# 1 = public
# 2 = archive
# 3 = private


class CreateNewPost(graphene.Mutation):
    class Input:
        title = graphene.NonNull(graphene.String)
        content = graphene.NonNull(graphene.String)
        excerpt = graphene.String()
        tags = graphene.List(graphene.String)
        category = graphene.String()
        link = graphene.String()
        visibilityId = graphene.Int()

    success = graphene.Boolean()

    @staticmethod
    def mutate(root, args, context, info):
        decoded = decode(context.headers.get('Authorization'))[0]
        if decoded is None:
            return CreateNewPost(success=False)
        userId = decoded['sub']
        user = User.get_query(context).get(userId)

        # begin creating the post
        try:
            new_post = Post(title=args['title'], content=args[
                            'content'], author=user)

            if 'excerpt' in args:
                new_post.excerpt = args['excerpt']
            if 'link' in args:
                new_post.link = args['link']
            # resolve visibility. default public
            new_post.visibilityId = args[
                'visibilityId'] if 'visibilityId' in args else 1

            # resolve tags
            tags = args['tags'] if 'tags' in args else []
            tagList = []
            for tag in tags:
                t = Tag.query.filter_by(name=tag).first()
                if t is None:
                    t = Tag(name=tag)  # create new tag if none exist
                tagList.append(t)
            new_post.tags = tagList

            # resolve category
            if 'category' in args:
                category = Category.query.filter_by(
                    name=args['category']).first()
                if category:
                    new_post.category = category

            # save the post to database
            db_session.add(new_post)
            db_session.commit()
            return CreateNewPost(success=True)

        except:
            return CreateNewPost(success=False)