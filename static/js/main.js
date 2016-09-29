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
        }
    },
    paths: {
        "angular": "bower_components/angular/angular",
        "jquery": "bower_components/jquery/dist/jquery.min",
        "bootstrap": "bower_components/bootstrap/dist/js/bootstrap.min",

        // application
        "LoginController": "application/controllers/Login/Login",
        "RegistrationController": "application/controllers/Registration/Registration"
    }
});

require(['angular'], function(ng){
    ng.module('Application', []);

    require(modules)
});