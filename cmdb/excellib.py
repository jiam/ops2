# -*- coding: utf-8 -*-
import json
import xlwt

def create_application_excel(objects):
    header_style = xlwt.easyxf(
    #'align: vertical center, horizontal center;'
    'align: wrap on;'
    'pattern: pattern solid, fore_colour gray_ega;'
    'font:  bold on;'
    'borders: top thin, bottom thin, left thin, right thin;'
    )
    book = xlwt.Workbook(encoding="utf-8")
    name = '应用系统等级表'
    sheet1 = book.add_sheet(name)
    sheet1.row(0).height_mismatch = True
    sheet1.row(0).height = 256 * 2
    sheet1.col(0).width = 256 * 30
    sheet1.col(1).width = 256 * 30
    sheet1.col(2).width = 256 * 30
    sheet1.col(3).width = 256 * 30
    sheet1.col(4).width = 256 * 30
    sheet1.col(5).width = 256 * 30
    sheet1.col(6).width = 256 * 30
    sheet1.col(7).width = 256 * 30
    sheet1.col(8).width = 256 * 30
    sheet1.col(9).width = 256 * 30
    sheet1.col(10).width = 256 * 30
    sheet1.col(11).width = 256 * 30
    sheet1.col(12).width = 256 * 30
    sheet1.col(13).width = 256 * 30
    sheet1.col(14).width = 256 * 30
    sheet1.col(15).width = 256 * 30
    sheet1.col(16).width = 256 * 30
    sheet1.col(17).width = 256 * 30
    sheet1.col(18).width = 256 * 30
    sheet1.col(19).width = 256 * 30
    sheet1.col(20).width = 256 * 30
    header = ['服务名','服务级别','一键发布','外网访问域名','内网访问域名','内部DNS域名','应用负责人','主机名','正向代理','nginx地址','内网IP','NAS的IP','keepalived的IP','执行应用的用户','应用路径与端口','配置文件','防火墙端口','涉及现金流量','用户量','重要的应用关联性','社会影响']
    
    for i in range(len(header)):
        sheet1.write(0,i,header[i],header_style)
    row = 1
    for object in objects:
        sheet1.write(row,0,object.service) 
        sheet1.write(row,1,object.service_level) 
        sheet1.write(row,2,object.auto_deploy) 
        sheet1.write(row,3,object.w_domain) 
        sheet1.write(row,4,object.l_domain) 
        sheet1.write(row,5,object.l_dns) 
        sheet1.write(row,6,object.app_user) 
        sheet1.write(row,7,object.hostname) 
        sheet1.write(row,8,object.proxy) 
        sheet1.write(row,9,object.nginx) 
        sheet1.write(row,10,object.lan_ip) 
        sheet1.write(row,11,object.nas_ip) 
        sheet1.write(row,12,object.keepalived_ip) 
        sheet1.write(row,13,object.exec_user) 
        sheet1.write(row,14,object.app_path_port) 
        sheet1.write(row,15,object.config_file) 
        sheet1.write(row,16,object.firewall_port) 
        sheet1.write(row,17,object.cash) 
        sheet1.write(row,18,object.user_num) 
        sheet1.write(row,19,object.key_app_related) 
        sheet1.write(row,20,object.internet_app) 
        row = row + 1
    return book,name
