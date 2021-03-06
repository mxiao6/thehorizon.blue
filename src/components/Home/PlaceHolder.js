import React, { PureComponent } from 'react';
import MediaQuery from 'react-responsive';

class PlaceHolder extends PureComponent {
    static routeConfig = {
        title: (
            <span>
                天际蓝
                <MediaQuery minDeviceWidth={768}>
                    {match => (match ? <span> | </span> : <br />)}
                </MediaQuery>
                thehorizon.blue
            </span>
        ),
        typingStrings: [
            '啊。^1000早上好，迷途中的旅者。^1000<br />欢迎来到天空的尽头。^1000',
            '前方是名为天际的一片虚无之地。^1000<br />藤蔓肆虐，荆棘丛生。',
            '那是不应被打扰的一片领域。',
            '因此^1000，请回吧。^500',
            '嗯？^1000执意前行吗？^1000<br />...真是没办法呢。^1000<br />那么^1000，请出示你的信物。^500',
            '祝你旅途愉快。',
        ],
    };

    render = () => {
        return <div />;
    };
}

export default PlaceHolder;
