# -*- coding: utf-8 -*-
from odoo.addons.portal.controllers.portal import CustomerPortal, pager
from odoo.http import request
from odoo import http, _
from odoo.tools import groupby as groupbylem
from operator import itemgetter

class VendorsForcatsPortal(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        rtn = super(VendorsForcatsPortal, self)._prepare_home_portal_values(counters)
        print("_prepare_portal_layout_values called", rtn)
        rtn['forcast_counts'] = request.env['vendor.forcast'].search_count([])
        return rtn

    @http.route(['/my/forcasts', '/my/forcats/page/<int:page>'], type='http', auth="user", website=True)
    def vendorforcastsListView(self, page=1, sortby='id', search="", search_in="All", groupby="none", **kw):

        if not groupby:
            groupby = 'none'
        sorted_list = {
            'id': {'label': 'ID', 'order': 'id'},
            'id_desc': {'label': 'ID Desc', 'order': 'id desc'},
            'product_id': {'label': 'Product', 'order': 'product_id'},
            'expected_quantity': {'label': 'Expected Quantity', 'order': 'expected_quantity'},
            'forecast_date': {'label': 'Forcast Date', 'order': 'forecast_date'}
        }

        search_list = {
            'All': {'label': 'All', 'input': 'All', 'domain':[]},
            'Quantity': {'label': 'Expected Quantity', 'input': 'Quantity', 'domain':[('expected_quantity','ilike',search)]},
            'Product': {'label': 'Product', 'input': 'Product', 'domain':[('product_id.name','ilike',search)]}
        }

        groupby_list = {
            'none': {'input':'none', 'label':_("None"), "order":1},
            'product_id': {'input':'product_id', 'label':_("Product"), "order":1},
        }
        forcast_group_by = groupby_list.get(groupby, {})
        search_domain = search_list[search_in]['domain']
        default_order_by = sorted_list[sortby]['order']
        if groupby in ("product_id"):
            forcast_group_by = forcast_group_by.get("input")
            default_order_by = forcast_group_by+","+default_order_by
        else:
            forcast_group_by = ''
        forcast_obj = request.env['vendor.forcast']
        total_forcasts = forcast_obj.sudo().search_count(search_domain)
        forcast_url = '/my/forcasts'
        page_detail = pager(url=forcast_url,
                            total=total_forcasts,
                            page=page,
                            url_args={'sortby': sortby, 'search_in': search_in, 'search': search, 'groupby':groupby},
                            step=10)
        forcasts = forcast_obj.sudo().search([], limit=10, order=default_order_by, offset=page_detail['offset'])
        if forcast_group_by:
            forcasts_group_list = [{forcast_group_by:k, 'forcasts':forcast_obj.concat(*g)} for k,g in groupbylem(forcasts, itemgetter(forcast_group_by))]
        else:
            forcasts_group_list = [{'forcasts':forcasts}]
        print(forcasts_group_list)
        vals = {
                #'forcasts': forcasts,
                'group_forcasts': forcasts_group_list,
                'page_name':'forcast_list_view', 'pager':page_detail,
                'default_url':forcast_url,
                'groupby': groupby,
                'sortby':sortby,
                'searchbar_sortings':sorted_list,
                'searchbar_groupby':groupby_list,
                'search_in':search_in,
                'searchbar_inputs':search_list,
                'search':search,
                }
        return request.render("vendors_self_service_portal.vendors_forcasts_list_view_portal", vals)


    @http.route(['/my/forcast/<model("vendor.forcast"):forcast_id>'], auth="user", type='http', website=True)
    def VendorForcastsFormView(self, forcast_id, **kw):
        vals = {"forcast": forcast_id, 'page_name': 'forcasts_form_view'}
        forcast_records = request.env['vendor.forcast'].search([])
        forcast_ids = forcast_records.ids
        forcast_index = forcast_ids.index(forcast_id.id)
        if forcast_index != 0 and forcast_ids[forcast_index - 1]:
            vals['prev_record'] = '/my/forcast/{}'.format(forcast_ids[forcast_index - 1])
        if forcast_index < len(forcast_ids) and forcast_ids[forcast_index + 1]:
            vals['next_record'] = '/my/forcast/{}'.format(forcast_ids[forcast_index + 1])
        return request.render("vendors_self_service_portal.vendor_forcast_form_view_portal", vals)

    @http.route(['/my/forcast/print/<model("vendor.forcast"):forcast_id>'], auth="user", type="http", website=True)
    def VendorForcastReportPrint(self, forcast_id, **kw):
        print("Hello this is called", forcast_id)
        return self._show_report(model=forcast_id, report_type='pdf', report_ref='vendors_self_service_portal.vendor_forcast_report', download=True)
