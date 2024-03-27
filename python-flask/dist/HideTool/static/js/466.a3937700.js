"use strict";(self["webpackChunkvue_axios"]=self["webpackChunkvue_axios"]||[]).push([[466],{4466:function(t,e,l){l.r(e),l.d(e,{default:function(){return d}});var a=function(){var t=this,e=t._self._c;return e("div",{staticClass:"home"},[e("div",{staticStyle:{height:"10px"}}),e("el-table",{attrs:{data:t.table,border:"",stripe:"",height:"680","cell-style":{textAlign:"center"},"header-cell-style":{textAlign:"center"}}},[e("el-table-column",{attrs:{prop:"folder",label:"文件夹",width:"250"}}),e("el-table-column",{attrs:{prop:"path",label:"路径"}}),e("el-table-column",{attrs:{prop:"hide",label:"隐藏",width:"60"}}),e("el-table-column",{attrs:{prop:"mask",label:"伪装",width:"120"}}),e("el-table-column",{attrs:{label:"操作",width:"210"},scopedSlots:t._u([{key:"default",fn:function(l){return[e("el-button",{attrs:{type:"info",size:"mini",icon:"el-icon-edit",round:""},on:{click:function(e){return t.handEdit(l.$index,l.row)}}},[t._v("编辑")]),e("el-popconfirm",{attrs:{title:"确认删除吗？",icon:"el-icon-info","icon-color":"#F56C6C"},on:{confirm:function(e){return t.handDelete(l.$index,l.row)}}},[e("el-button",{attrs:{slot:"reference",type:"danger",size:"mini",icon:"el-icon-delete",round:""},slot:"reference"},[t._v("删除")])],1)]}}])},[e("template",{slot:"header"},[e("el-row",{attrs:{type:"flex",justify:"center"}},[e("el-col",{attrs:{span:10}},[e("span",{staticClass:"op"},[t._v("操作")])]),e("el-col",{attrs:{span:8}},[e("el-button",{staticClass:"add",attrs:{size:"mini",icon:"el-icon-plus"},on:{click:t.addDialog}},[t._v("添加")])],1)],1)],1)],2)],1),e("el-dialog",{attrs:{title:"文件夹设置",visible:t.dialogVisible,width:"30%","before-close":t.handleClose}},[e("el-form",{ref:"form",attrs:{model:t.form,"status-icon":"",rules:t.rules,"label-width":"60px"}},[e("el-form-item",{attrs:{label:"文件夹",prop:"folder"}},[e("el-input",{attrs:{autocomplete:"on",disabled:""},model:{value:t.form.folder,callback:function(e){t.$set(t.form,"folder",e)},expression:"form.folder"}})],1),e("el-form-item",{attrs:{label:"路径",prop:"path"}},[e("el-input",{attrs:{autocomplete:"on",disabled:""},model:{value:t.form.path,callback:function(e){t.$set(t.form,"path",e)},expression:"form.path"}})],1),e("el-form-item",{attrs:{label:"隐藏"}},[e("el-switch",{attrs:{autocomplete:"on","active-value":"是","inactive-value":"否"},model:{value:t.form.hide,callback:function(e){t.$set(t.form,"hide",e)},expression:"form.hide"}})],1),e("el-form-item",{attrs:{label:"伪装",prop:"mask"}},[e("el-select",{attrs:{autocomplete:"on"},model:{value:t.form.mask,callback:function(e){t.$set(t.form,"mask",e)},expression:"form.mask"}},t._l(t.mask_select,(function(t){return e("el-option",{key:t.label,attrs:{label:t.label,value:t.value}})})),1)],1)],1),e("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[e("el-button",{attrs:{type:"primary"},on:{click:t.edit}},[t._v("确定")])],1)],1),e("el-dialog",{attrs:{title:"添加文件夹",visible:t.addVisible,width:"30%","before-close":t.addClose}},[e("el-form",{ref:"form",attrs:{model:t.form,"status-icon":"",rules:t.rules,"label-width":"60px"}},[e("el-form-item",{attrs:{label:"文件夹",prop:"folder"}},[e("el-row",[e("el-col",{attrs:{span:16}},[e("el-input",{attrs:{disabled:""},model:{value:t.form.folder,callback:function(e){t.$set(t.form,"folder",e)},expression:"form.folder"}})],1),e("el-col",{attrs:{span:8}},[e("center",[e("el-button",{on:{click:t.sel}},[t._v("选择")])],1)],1)],1)],1),e("el-form-item",{attrs:{label:"路径",prop:"path"}},[e("el-input",{attrs:{disabled:""},model:{value:t.path_get,callback:function(e){t.path_get=e},expression:"path_get"}})],1),e("el-form-item",{attrs:{label:"隐藏"}},[e("el-switch",{attrs:{"active-value":"是","inactive-value":"否"},model:{value:t.hide_get,callback:function(e){t.hide_get=e},expression:"hide_get"}})],1),e("el-form-item",{attrs:{label:"伪装",prop:"mask"}},[e("el-select",{model:{value:t.mask_get,callback:function(e){t.mask_get=e},expression:"mask_get"}},t._l(t.mask_select,(function(t){return e("el-option",{key:t.label,attrs:{label:t.label,value:t.value}})})),1)],1)],1),e("span",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[e("el-button",{attrs:{type:"primary"},on:{click:t.add}},[t._v("确定")])],1)],1)],1)},i=[],o={name:"Home",data(){return{table:[],dialogVisible:!1,addVisible:!1,routeDialogVisible:!0,form:{},rules:{},path_get:null,mask_get:"无",hide_get:"否",mask_select:[{label:"无",value:"无"},{label:"无关联文件",value:"无关联文件"},{label:"回收站",value:"回收站"},{label:"脱机文件夹",value:"脱机文件夹"},{label:"管理工具",value:"管理工具"},{label:"历史记录",value:"历史记录"},{label:"缓存文件夹",value:"缓存文件夹"},{label:"拨号网络",value:"拨号网络"},{label:"网上邻居",value:"网上邻居"}]}},created(){this.init()},methods:{init(){this.$axios.get("/all").then((t=>{this.table=t.data}))},sel(){this.$axios.get("/sel").then((t=>{this.path_get=t.data["path"],this.form.folder=t.data["folder"],this.form.path=this.path_get}))},addDialog(){this.addVisible=!0,this.form={}},handEdit(t,e){this.dialogVisible=!0,this.form=JSON.parse(JSON.stringify(e))},handDelete(t,e){let l=JSON.parse(JSON.stringify(e)).path;this.$axios.post("/delete",{path:l}).then((t=>{200==t.code?(this.$notify.success({title:"成功",message:t.msg,duration:1e3,position:"bottom-right"}),this.init()):this.$notify.success({title:"失败",message:t.msg,duration:2e3,position:"bottom-right"})}))},handleClose(){this.dialogVisible=!1,this.init()},addClose(){this.addVisible=!1,this.path_get=null,this.hide_get="否",this.init()},edit(){this.$axios.post("/update",this.form).then((t=>{200==t.code?(this.handleClose(),this.$notify.success({title:"成功",message:t.msg,duration:1e3,position:"bottom-right"})):this.$notify.error({title:"错误",message:t.msg,duration:2e3,position:"bottom-right"})}))},add(){"path"in this.form?(this.form.mask=this.mask_get,this.form.hide=this.hide_get,this.$axios.post("/add",this.form).then((t=>{this.form={},this.path_get=null,this.mask_get="无",this.hide_get="否",200==t.code?(this.addClose(),this.$notify.success({title:"成功",message:t.msg,duration:1e3,position:"bottom-right"})):this.$notify.error({title:"错误",message:t.msg,duration:2e3,position:"bottom-right"})}))):this.$notify.error({title:"错误",message:"未选择文件夹",duration:2e3,position:"bottom-right"})}}},s=o,r=l(1001),n=(0,r.Z)(s,a,i,!1,null,null,null),d=n.exports}}]);