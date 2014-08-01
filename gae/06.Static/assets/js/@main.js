$(function(){
    var ModoScript = Backbone.Model.extend({
        initialize: function() {
            console.log("ModoScript#init");
        }
    });

    var ModoScriptList = Backbone.Collection.extend({
        model: ModoScript,
        url: "http://localhost:8080/",
        parse: function(res) {
            return res;
        }
    });

    var ModoScriptView = Backbone.View.extend({
        el: "#modo-script-list",
        initialize: function() {
            console.log("ModoScriptView#init")
            this.collection = new ModoScriptList();
            this.collection.fetch();
        },
        events: {
            "click button": "render"
        },
        render: function(e) {
            var str = "";
            var mo = this.collection.models;
            for (var i = 0, max = mo.length; i < max; i++) {
                str += this.template(mo[i]);
            }
            $(this.el).html(str);
        },
        template: function(script) {
            var str = "<tr>"
                + '<td>' + script.get("name") + '</td>'
                + '<td>' + script.get("rating") + '</td>'
                + '<td>' + script.get("author") + '</td>'
                + '<td><button class="btn btn-mini">detail</button></td>'
                + '</tr>';

            return str
        }
    });
    var view = new ModoScriptView();
});
