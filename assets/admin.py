from django.contrib import admin
from assets import models
from assets import asset_handler


class NewAssetAdmin(admin.ModelAdmin):
    # 展示字段
    list_display = ['asset_type', 'sn', 'model', 'manufacturer', 'c_time', 'm_time']
    # 过滤字段
    list_filter = ['asset_type', 'manufacturer', 'c_time']
    # 搜索字段
    search_fields = ('sn',)
    # 自定义行为
    actions = ['approve_selected_new_assets']
    def approve_selected_new_assets(self,request,queryset):
        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        success_upline_number = 0
        for asset_id in selected:
            obj = asset_handler.ApproveAsset(request,asset_id)
            ret = obj.asset_upline()
            if ret:
                success_upline_number += 1

        self.message_user(request,"成功批准  %s  条新资产上线！" % success_upline_number)

    approve_selected_new_assets.short_description = "批准选择的新资产"



class AssetAdmin(admin.ModelAdmin):
    list_display = ['asset_type', 'name', 'status', 'approved_by', 'c_time', "m_time"]


class ListAdmin(admin.ModelAdmin):
    list_display = ['asset','model','created_by','hosted_on']

class Issue_deal(admin.ModelAdmin):
    list_display = ['asset','date','user']
admin.site.register(models.Asset, AssetAdmin)
admin.site.register(models.Server,ListAdmin,)
admin.site.register(models.StorageDevice)
admin.site.register(models.SecurityDevice)
admin.site.register(models.BusinessUnit)
admin.site.register(models.Contract)
admin.site.register(models.CPU)
admin.site.register(models.Disk)
admin.site.register(models.EventLog,Issue_deal)
admin.site.register(models.IDC)
admin.site.register(models.Manufacturer)
admin.site.register(models.NetworkDevice)
admin.site.register(models.NIC)
admin.site.register(models.RAM)
admin.site.register(models.Software)
admin.site.register(models.Tag)
admin.site.register(models.NewAssetApprovalZone, NewAssetAdmin)
