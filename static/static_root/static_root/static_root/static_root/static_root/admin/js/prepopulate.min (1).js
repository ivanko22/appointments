(function(b){b.fn.prepopulate=function(e,g){return this.each(function(){var a=b(this),d=function(){if(!a.data("_changed")){var f=[];b.each(e,function(h,c){c=b(c);c.val().length>0&&f.push(c.val())});a.val(URLify(f.join(" "),g))}};a.data("_changed",false);a.change(function(){a.data("_changed",true)});a.val()||b(e.join(",")).keyup(d).change(d).focus(d)})}})(django.jQuery);