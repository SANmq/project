(function () {
    // 这里设置当天时间的方法
    function setTime() {
        let a = $(".now div").eq(1)
            .text(getTime(beforeToday(1)).date)
            .siblings().eq(1).text(getTime(beforeToday(1)).datetime)
    }

    setTime()
    setInterval(setTime, 1000)
    //----------------------------------------------

    $('.layout > div:nth-child(3) > ul > li').click(function () {
        if ($(this).hasClass("select")) {
            return false
        }
        $(this).addClass("select").siblings().removeClass("select")
        renderTable($(this).attr("bind"))
    })
    // 字段切换功能
    $("#changeCol").click(function () {
        let tableName = $(".layout .select").attr("bind")
        if (tableName === "单品销售对比") {
            $('.tb1 thead .show')



        }


    })
    // 查找功能
    $("#select").click(
        function () {
            let selectTb = $('.layout > div:nth-child(3) > ul > li.select').attr("bind")
            let data = {}
            if (selectTb === "单品销售展示") {
                let t0 = $("#t0").val().split("~"),
                    goodID = $("goodFilter").val()
                data.t0 = t0[0]
                data.t1 = t0[1]
                if (/\d+/g.test(goodID)) {
                    data.goodID = goodID
                }
            }
            console.log(data)
            renderTable(selectTb, data)
        }
    )

    function renderTable(tableName, data) {
        data = data || {}
        console.log('/rpt/api/' + tableName)
        $.post(
            {
                data: data,
                url: '/rpt/api/' + tableName,
                success: function (data) {
                    $("#goodFilter").val(data.hasOwnProperty("goodName") ? data["goodName"] : "")
                    $("#t0").val(data.hasOwnProperty("tRound1") ? data["tRound1"] : "")
                    $("#t1").val(data.hasOwnProperty("tRound2") ? data["tRound2"] : "")
                    $('.layout .tableArea').html("").html(data["renderTable"])
                    console.log(data)
                }
            }
        )
    }

    // 初始化渲染页面
    renderTable($('.layout > div:nth-child(3) ul li.select').attr("bind"))


}())

