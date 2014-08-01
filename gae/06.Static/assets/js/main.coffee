jQuery ->
  class ModoScript extends Backbone.Model
    initialize: ->
      console.log("ModoScript#init")
      return

  class ModoScriptList extends Backbone.Collection
    model: ModoScript
    url: "http://localhost:8080/"
    parse: (res) ->
      return res

  class ModoScriptView extends Backbone.View
    el: "#modo-script-list"

    initialize: ->
      console.log("ModoScriptView#init")
      @collection = new ModoScriptList()
      @collection.fetch()
      return

    events: {
      "click button": "render"
    }

    render: (e) ->
      str = ""
      mo = @collection.models
      for key, element of mo
        str += @template(element[key])
      $(@el).html(str)
      return

    template: (script) ->
      str += "<tr>"
      + '<td>' + script.name + '</td>'
      + '<td>' + script.rating + '</td>'
      + '<td>' + script.updated + '</td>'
      + '<td><button class="btn btn-mini">detail</button></td>'
      + '</tr>';
      return str

  view = new ModoScriptView()