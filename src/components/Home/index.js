import React, { Component } from 'react';
import { gql, graphql } from 'react-apollo';
import { bind as Mousetrap } from 'mousetrap';
import Anime from 'react-anime';

import './style.css';

@graphql(gql`query { test }`)
class Home extends Component {
  componentWillMount() {
    // The special hotkeys to enter the main website
    Mousetrap('up down left right up down left right', () =>
      this.props.history.push('/about')
    );
  }
  render() {
    const { data: { test } } = this.props;
    return (
      <Anime opacity={[0, 1]} translateY={'1em'} delay={(e, i) => i * 500}>
        <p className="App-intro">
          之前一直想写一个<del>酷炫</del>的个人网站，然而一直未果。正好最近在折腾<code>React Native</code>，就想着顺手用<code>React</code>把天际林整理一下好了。
        </p>
        <p className="App-intro">
          你现在看到的只是<del>又一个</del>占位置的首页，具体内容最近会抽空更新。在此之前，欢迎去原博客<a href="http://www.forestofhorizon.com/">天际林</a>转转。
        </p>
        <p className="App-intro">
          回见。
        </p>
        <p className="App-intro">
          — 蓝色天际 | {test}—
        </p>
      </Anime>
    );
  }
}

export default Home;
