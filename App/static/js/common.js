$('.total').click(function () {
    let data = $(this).data()
    if (data["ckCount"]) {
        data["ckCount"] += 1
    } else {
        data["ckCount"] = 1
    }
    setTimeout(() => {
        data["ckCount"] = 0
    }, 500)
    if (data["ckCount"] === 2) {
        if (this.className.indexOf('off') >= 0) {
            $(this).removeClass('off').addClass('on')
        } else {
            $(this).removeClass('on').addClass('off')
        }
    }
})

function beforeToday(delta) {
    let day = new Date(),
        nowTime = day.getTime(),
        ms = 24 * 3600 * 1000 * delta;
    day.setTime(nowTime - ms);
    return day
}

function getTime(time) {
    let T = time,
        Y = T.getFullYear(),
        M = T.getMonth() > 8 ? (T.getMonth() + 1).toString() : '0' + (T.getMonth() + 1).toString(),
        D = T.getDate() > 9 ? T.getDate().toString() : '0' + T.getDate().toString(),
        h = T.getHours() > 9 ? T.getHours().toString() : '0' + T.getHours().toString(),
        m = T.getMinutes() > 9 ? T.getMinutes().toString() : '0' + T.getMinutes().toString(),
        s = T.getSeconds() > 9 ? T.getSeconds().toString() : '0' + T.getSeconds().toString(),
        date = Y + '-' + M + '-' + D,
        datetime = h + ':' + m + ':' + s
    return {date, datetime}
}