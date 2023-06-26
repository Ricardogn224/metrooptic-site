function redirectMobile(isMobile) {
    const path = window.location.pathname;

    if (isMobile) {
        switch (path) {
            case '/':
                window.location.href = '/phone_home';
                break;
            case '/FTTH_pro':
                window.location.href = '/phone_ftth';
                break;
            case '/FTTO_pro':
                window.location.href = '/phone_ftto';
                break;
            case '/iot':
                window.location.href = '/phone_iot';
                break;
            case '/contact':
                window.location.href = '/phone_contact';
                break;
            case '/data_center':
                window.location.href = '/phone_data';
                break;
            case '/solution_data':
                window.location.href = '/phone_4G_5G';
                break;
            case '/securite':
                window.location.href = '/phone_securite';
            default:
                break;
        }
    }

    else {
        switch (path) {
            case '/phone_home':
                window.location.href = '/';
                break;
            case '/phone_ftth':
                window.location.href = '/FTTH_pro';
                break;
            case '/phone_ftto':
                window.location.href = '/FTTO_pro';
                break;
            case '/phone_iot':
                window.location.href = '/iot';
                break;
            case '/phone_contact':
                window.location.href = '/contact';
                break;
            case '/phone_data':
                window.location.href = '/data_center';
            case '/phone_4G_5G':
                window.location.href = '/solution_data';
                break;
            case '/phone_securite':
                window.location.href = '/securite';
            default:
                break;
        }
    }
}

function checkMobileScreenSize() {
    var screenWidth = window.innerWidth || document.documentElement.clientWidth || document.body.clientWidth;

    if (screenWidth < 768) {
        redirectMobile(true);
        console.log('Phone size');
    } else {
        redirectMobile(false);
        console.log('Desktop size');
    }
}

window.addEventListener('resize', checkMobileScreenSize);
window.addEventListener('load', checkMobileScreenSize);
