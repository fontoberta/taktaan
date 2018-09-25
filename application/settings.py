settings = {
    'devel' : {
        'boon_token_validation_url' : 'standalone',
        'boon_get_token_url' : 'standalone',
        'docker_unix_url' : 'unix://var/run/docker.sock',
        'test_username' : 'admin',
        'test_password' : 'administrator',
        'test_client_id' : 'YoYIt7U2Pplib7zyDt8XmFXVo0seTg0INYkmj3rn',
        'test_token' : ''
    },

    'prod': {
        'boon_token_validation_url' : 'http://boon-service:8000/validate-token/',
        'boon_get_token_url' : 'http://boon-service:8000/oauth/token/',
        'docker_unix_url' : 'unix://var/run/docker.sock',
        'test_username' : 'admin',
        'test_password' : 'administrator',
        'test_client_id' : 'YoYIt7U2Pplib7zyDt8XmFXVo0seTg0INYkmj3rn',
        'test_token' : ''

    }

}
