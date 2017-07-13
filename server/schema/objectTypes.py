import models
from graphene_sqlalchemy import SQLAlchemyObjectType
from sqlalchemy import and_, or_
from .utils import Utils, decode


class User(Utils, SQLAlchemyObjectType):
    class Meta:
        model = models.User
        exclude_fields = ['password', 'deleted', 'groupId']


class Post(Utils, SQLAlchemyObjectType):
    class Meta:
        model = models.Post
        exclude_fields = ['deleted', 'authorId', 'categoryId']

    @classmethod
    def get_all(cls, context):
        token = context.headers.get('Authorization')
        decoded = decode(token)[0]
        model = cls._meta.model
        if decoded is None:
            return model.query.filter(model.deleted == False, model.visibilityId != 4).order_by(model.publishDate.desc()).all()
        userId = decoded.get('sub')
        return model.query.filter(and_(model.deleted == False, or_(model.visibilityId != 4, model.authorId == userId))).order_by(model.publishDate.desc()).all()


class Comment(Utils, SQLAlchemyObjectType):
    class Meta:
        model = models.Comment
        exclude_fields = ['deleted', 'authorId', 'postId', 'parentId']


class Tag(Utils, SQLAlchemyObjectType):
    class Meta:
        model = models.Tag
        exclude_fields = ['deleted']


class Category(Utils, SQLAlchemyObjectType):
    class Meta:
        model = models.Category
        exclude_fields = ['deleted']


class Group(Utils, SQLAlchemyObjectType):
    class Meta:
        model = models.Group
        exclude_fields = ['deleted']
