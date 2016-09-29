module.exports = function (grunt) {

    require('load-grunt-tasks')(grunt);

    grunt.initConfig({
        less: {
            mobile: {
                paths: ['static/css'],
                files: {
                    'static/css/app.css': 'static/css/less/main.less'
                }
            }
        },
        watch: {
            less: {
                files: 'static/css/**/*.less',
                tasks: ['less:mobile'],
                options: {
                    nospawn: true
                }
            }
        }
    });

    grunt.registerTask('default', ['watch']);
};