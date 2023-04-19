var minutes;
var seconds;
var set_inteval;
function otp_timer() {
    if (seconds == 0 & minutes == 0) {
        document.getElementById('seconds').innerHTML = '00';
        document.getElementById('minutes').innerHTML = '0';
        document.getElementById('regesterbuttonrepeat').disabled = false;
        document.getElementById('regesterbuttonsave').disabled = true;

    } else {
        seconds -= 1;
        document.getElementById('seconds').innerHTML = seconds;
        document.getElementById('minutes').innerHTML = minutes;
            if (seconds == 0) {
            if (minutes > 0) {
                seconds = 60;
                minutes -= 1;
            } else {
                document.getElementById("sendButton1").disabled = true;
                minutes = 0;
                document.getElementById('minutes').innerHTML = minutes;
                clearInterval(set_inteval);
                minutes = 0;
                seconds = 0;
                document.getElementById('seconds').innerHTML = '00';
                document.getElementById('minutes').innerHTML = '0';
            }
        }
    }
}
function startTimer()
{
    document.getElementById('regesterbuttonrepeat').disabled = true;
    ocument.getElementById('regesterbuttonsave').disabled = false;
    minutes = 1;
    seconds = 59;
    document.getElementById('seconds').innerHTML = seconds;
    document.getElementById('minutes').innerHTML = minutes;
    set_inteval = setInterval( 'otp_timer()', 1000 );
}
startTimer();

