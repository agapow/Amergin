/*
 * JX 0.6  - 24 Mar 2009
 * Copyright(c) 2008, Santosh Rajan
 * Author: Santosh Rajan
 * Email: santrajan@gmail.com
 * License: Dual License - MIT, GPL
 */

var JX = {

    extend: function(bc, sc, o) {
        var f = function() {};
        f.prototype = sc.prototype;
        bc.prototype = new f();
        bc.prototype.constructor = bc;
        bc.superclass = sc.prototype;
        for (var m in o)
            bc.prototype[m] = o[m];
    },

    setScope: function(callback, scope) {
        return function() {
            return callback.apply(scope, arguments);
        };
    },

    namespace: function() {
        var ns, d;
        for (var i = 0; i < arguments.length; i++) {
            ns = window;
            d = arguments[i].split(".");
            for (var j in d)
                ns = ns[d[j]] = ns[d[j]] ? ns[d[j]] : {};
        };
    },
    
    isObject: function(obj) {
        return (obj && obj.constructor && obj.constructor == Object.prototype.constructor && !obj.nodeName)
            ? true : false;
    },
    
    jxTypes: {
        component: 'JX.Component',
        container: 'JX.Container',
        columncontainer: 'JX.ColumnContainer',
        selectfield: 'JX.SelectField',
        textfield: 'JX.TextField',
        buttonfield: 'JX.ButtonField'
    }
};

JX.Component = function() {
    if (JX.isObject(arguments[0])) {
        var config = arguments[0];
        config.jxtype = config.jxtype ? config.jxtype : 'div'; // default type is div
        config.jxtype = JX.jxTypes[config.jxtype] ? 'div' : config.jxtype;
        JX.Component.superclass.init.call(this, document.createElement(config.jxtype));
        this.applyConfig(config);
    } else {
        if (arguments.length > 0)
            JX.Component.superclass.init.apply(this, arguments);
        else
            JX.Component.superclass.init.call(this, document.createElement('div'));
    }
    this[0]._jx = this;
};

JX.extend(JX.Component, jQuery, {
    applyConfig: function(config) {
        var a;
        this.css({overflow: 'hidden'});
        for (var key in config) {
            a = jQuery.isArray(config[key]) ? config[key] : [config[key]];
            for (var i = 0; i < a.length; i++)
                if (config.scopeThis)
                    a[i] = (typeof a[i] == 'function') ? JX.setScope(a[i], this) : a[i];
            eval('this.' + key + '.apply(this, a)');
        };
    },
    jxtype: function(jxtype) { 
        this._jxtype = jxtype;
    },
    fitWidth: function(fit) {
        this._fitWidth = fit;
        return this;
    },
    fitHeight: function(fit) {
        this._fitHeight = fit;
        return this;
    },
    scopeThis: function(s) {
        this._scope = s;
    },
    fieldName: function(f) {
        this._fieldName = f;
    },
    appendTo: function(obj) {
        JX.Component.superclass.appendTo.call(this, obj);
        this.height(obj.height());
        this.width(obj.width());
    },
    setLoadIndicator: function(url, w, h) {
        var s;
        this.children().each(function() {$(this).remove()});
        var top = (s = parseInt(this.height()/2 - h/2)) < 0 ? '0px' : s + 'px';
        var left = (s = parseInt(this.width()/2 - w/2)) < 0 ? '0px' : s + 'px';
        JX.Component.prototype.append.call(this, new JX.Component({
            jxtype: 'image',
            attr: {src: url},
            css: {
                position: 'relative',
                top: top,
                left: left
            }
        }));
    },
    removeLoadIndicator: function() {
        this.children().each(function() {$(this).remove()});
    },
    spacingHeight: function() {
        var ret = 0, s;
        ret += isNaN(s = parseInt(this.css('borderTopWidth'))) ? 0 : s;
        ret += isNaN(s = parseInt(this.css('borderBottomWidth'))) ? 0 : s;
        ret += isNaN(s = parseInt(this.css('paddingTop'))) ? 0 : s;
        ret += isNaN(s = parseInt(this.css('paddingBottom'))) ? 0 : s;
        return ret;
    },    
    spacingWidth: function() {
        var ret = 0, s;
        ret += isNaN(s = parseInt(this.css('borderLeftWidth'))) ? 0 : s;
        ret += isNaN(s = parseInt(this.css('borderRightWidth'))) ? 0 : s;
        ret += isNaN(s = parseInt(this.css('paddingLeft'))) ? 0 : s;
        ret += isNaN(s = parseInt(this.css('paddingRight'))) ? 0 : s;
        return ret;
    },
    draggable: function(config) {
        if ($('#jxdraghelper')[0] == undefined) 
            $('body').append('<div id="jxdraghelper"></div>');
        var config = jQuery.extend({
            appendTo: '#jxdraghelper',
            helper: 'clone',
            revert: 'invalid',
            opacity: 0.7,
            containment: 'body'
        }, config);
        JX.Component.superclass.draggable.call(this, config);
    }
});


JX.Container = function() {
    this._items = [];
    JX.Container.superclass.constructor.apply(this, arguments);
};
JX.extend(JX.Container, JX.Component, {
    applyConfig: function(config) {
        JX.Container.superclass.applyConfig.apply(this, arguments);
        var c = this.citems ? this.citems : [], item, obj;
        for (var i = 0; i < c.length; i++) {
            item = c[i];
            if (JX.isObject(item)) {
                item.jxtype = item.jxtype ? item.jxtype : 'div';
                if (JX.jxTypes[item.jxtype])
                    eval('obj = new ' + JX.jxTypes[item.jxtype] + '(item)');
                else
                    obj = new JX.Component(item);
            } else
                obj = item;
            this.append(obj);
        };
    },
    append: function(comp) {
        JX.Container.superclass.append.apply(this, arguments);
        if (comp instanceof JX.Component) {
            this._items.push(comp);
            comp._parent = this;
            comp._idx = this._items.length - 1;
        };
        return this;
    },
    items: function() {
        this.citems = Array.prototype.slice.call(arguments);
    },
    onLayout: function(func) {
        this._onLayout = func;
    },
    doLayout: function() {
        if (this._onLayout)
            this._onLayout();
        var h = this.height(), fitter, el;
        if (this.is(':hidden')) return;
        for (var i = 0; i < this._items.length; i++) {
            el = this._items[i];
            if (el.is(':hidden')) continue;
            if (el._fitWidth)
                el.width(this.width() - el.spacingWidth());
            if (el._fitHeight) {
                fitter = el;
                h -= el.spacingHeight();
            } else {
                h -= el.outerHeight();
            }
        };
        if (fitter) {
            fitter.height(h);
        }
        for (var i in this._items) {
            el = this._items[i];
            if (el.doLayout)
                JX.setScope(el.doLayout, el)();
        };
        return this;
    },
    getItems: function() {
        return this._items;
    },
    trigger: function() {
        JX.Container.superclass.trigger.apply(this, arguments);
        if (this._items)
            for (var i = 0; i < this._items.length; i++)
                this._items[i].trigger.apply(this._items[i], arguments);
    },
    removeItem: function(idx) {
        var a = this._items;
        a[idx].remove();
        a.splice(idx, 1);
        this.setItemIndex();
    },
    droppable: function(config) {
        this._drop = config.drop ? config.drop : null;
        delete config.drop;
        var config = jQuery.extend({
            accept: function() {return true;},
            drop: JX.setScope(this.drop, this)
        }, config);
        JX.Container.superclass.droppable.call(this, config);
    },
    drop: function(e, ui) {
        var dragitem = ui.draggable[0]._jx;
        if (this._drop) {
            this._drop(e, ui, dragitem, this);
            return;
        };
        var d = ui.position, a = this._items, p;
        for (var i = 0; i < a.length; i++) {
            p = a[i].position();
            if (this.isLess(d, p))
                break;
        };
        dragitem._parent.removeItem(dragitem._idx);
        this.insertAt(dragitem, i);
        this.dragEnable(dragitem);
    },
    dragEnable: function(comp) {
        comp.draggable('enable');
    },
    isLess: function(d, p) {
        return (d.top < p.top);
    },
    insertAt: function(comp, idx) {
        var a = this._items;
        if (idx == a.length || a.length == 0) {
            this.append(comp);
            return;
        };
        comp._parent = this;
        a.splice(idx, 0, comp);
        this.setItemIndex();
        this.insertItemBefore(comp, idx + 1);
    },
    insertItemBefore: function(comp, idx) {
        this._items[idx].before(comp);
    },
    setItemIndex: function() {
        var a = this._items;
        for (var i = 0; i < a.length; i++)
            a[i]._idx = i;
    }
});


JX.ColumnContainer = function() {
    if (arguments.length > 0)
        JX.ColumnContainer.superclass.constructor.apply(this, arguments);
    else
        JX.ColumnContainer.superclass.constructor.call(this, {});
    this._gridfix = 0;
};
JX.extend(JX.ColumnContainer, JX.Container, {
    applyConfig: function(config) {
        $('<table border="0px" cellspacing="0px" cellpadding="0px"><tr></tr></table>').appendTo(this);
        JX.ColumnContainer.superclass.applyConfig.apply(this, arguments);
    },
    append: function(comp) {
        $('tr:first', this).append($(document.createElement('td')).append(comp));
        if (comp instanceof JX.Component) {
            this._items.push(comp);
            comp._parent = this;
            comp._idx = this._items.length - 1;
        };
        return this;
    },
    doLayout: function() {
        if (this._onLayout)
            this._onLayout();
        var height = this.height(), fitter, el;
        var width = this.width();
        if (!width) return;
        for (var i = 0; i < this._items.length; i++) {
            el = this._items[i];
            if (el._fitHeight)
                el.height(height - el.spacingHeight());
            if (el._fitWidth) {
                fitter = el;
                width -= el.spacingWidth() + this._gridfix;
                if (this._gridfix)
                    this.width(this.width() - this._gridfix);
            } else
                width -= el.outerWidth();
        };
        if (fitter)
            fitter.width(width);
        for (var i = 0; i < this._items.length; i++) {
            el = this._items[i];
            if (el.doLayout)
                JX.setScope(el.doLayout, el)();
        };
        return this;
    },
    removeItem: function(idx) {
        var td = $(':parent:first', this._items[idx]);
        JX.ColumnContainer.superclass.removeItem.call(this, idx);
        td.remove();
    },
    gridfix: function(w) { //private
        this._gridfix = w;
    },
    isLess: function(d, p) {
        return (d.left < p.left);
    },
    insertItemBefore: function(comp, idx) {
        $('td', this).remove();
        var a = this._items.slice();
        this._items = [];
        for (var i = 0; i < a.length; i++) {
            this.append(a[i]);
        };
    },
    dragEnable: function(comp) {
        for (var i = 0; i < this._items.length; i++)
            this._items[i].draggable('enable');
    }
});



JX.Viewport = function() {
    JX.Viewport.superclass.constructor.call(this, document.body);
    this.children().each(function() {$(this).hide()});
    this.css({padding: '0px', margin: '0px'});
    this.setSize();
    $(window).resize(JX.setScope(this.setSize, this));
    if (JX.isObject(arguments[0])) {
        this.applyConfig(arguments[0]);
        this.setSize();
    };
};
JX.extend(JX.Viewport, JX.Container, {
    setSize: function() {
        this.height($(window).height() || window.innerHeight);
        this.width($(window).width());
        this.doLayout();
    }
});
// Forms

JX.TextField = function(config) {
	config = config ? config : {};
	config.jxtype = 'input';
	JX.TextField.superclass.constructor.call(this, config);
    this.attr({type: "text"});
};
JX.extend(JX.TextField, JX.Component, {
});

JX.SelectField = function(config) {
	config = config ? config : {};
	config.jxtype = 'select';
	JX.SelectField.superclass.constructor.call(this, config);
};
JX.extend(JX.SelectField, JX.Component, {
});

JX.ButtonField = function(config) {
	config = config ? config : {};
	config.jxtype = 'input';
	JX.ButtonField.superclass.constructor.call(this, config);
    this.attr({type: "button"});
};
JX.extend(JX.ButtonField, JX.Component, {
});

