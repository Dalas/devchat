require.config({
    shim: {
        "angular": {
            exports: 'angular'
        },
        "angular-modals": {
            deps: ['angular']
        },
        "bootstrap": {
            deps: ['jquery']
        },
        "bootstrap-material": {
            deps: ['bootstrap']
        }
    },
    paths: {
        "angular": "bower_components/angular/angular",
        "jquery": "bower_components/jquery/dist/jquery.min",
        "bootstrap": "bower_components/bootstrap/dist/js/bootstrap.min",
        "material": "bower_components/bootstrap-material-design/js/base"
    }
});

require(['angular', 'jquery'], function(ng, $){
    $.material.init();
    ng.module('Application', []);

    require(modules)
});