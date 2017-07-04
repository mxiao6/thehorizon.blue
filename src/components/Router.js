import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';
import Home from './Home';
import About from './About';
import NotFound from './NotFound';

class Router extends Component {
    render() {
        return (
            <Switch>
                <Route path="/" exact component={Home} />
                <Route path="/about" component={About} />
                <Route component={NotFound} />
            </Switch>
        );
    }
}

export default Router;