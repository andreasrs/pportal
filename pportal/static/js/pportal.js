define(['jquery', 'bootstrap', 'js/tweetbox'], function($, bootstrap, tweetbox) {
    var Pportal = {
        start: function() {
            tweetbox.attach('#tweetbox');
        }
    }

    return Pportal;
});
