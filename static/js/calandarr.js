 function yearselect(v) {
    console.log(v);
    a = v /1000;
    console.log(a);
    if (a >= 1 ){
        Swal.fire({
          position: 'top-end',
          icon: 'success',
          title: m + 'جند لحظه صبر کنید',
          showConfirmButton: false,
          timer: 2000
                 });

        // document.getElementsByClassName('textobject')[0].innerHTML = 'تقویم';
        // document.getElementsByClassName('calanderhead')[0].hidden = false;
        // document.getElementsByClassName('calandeer')[0].hidden = false;
        f = document.getElementById("face");
        f.click();
    }
 }
