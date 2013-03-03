define(['jquery'], function($) {
    return {
        attach: function(selector) {
            this.api(selector);
        },

        api: function(selector) {
            var twitter_api_url = 'http://search.twitter.com/search.json';
             
            $.getJSON(
                twitter_api_url + '?callback=?&rpp=5&q=python,django',

                function(data) {

                    $.each(data.results, function(i, tweet) {
                        if(tweet.text !== undefined) {
                            var date_tweet = new Date(tweet.created_at);
                            var date_now   = new Date();
                            var date_diff  = date_now - date_tweet;

                            var tweet = $('<div>').attr('class', 'tweet').html(tweet.text);

                            $(selector).append(tweet);
                        }
                    });
            });
        }
    };
});
