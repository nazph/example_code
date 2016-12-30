"""select nt_btcom.code as "ma_btcom",nt_btcom.name as "btcom",
nt.code as "ma_tinh",nt.name as "tinh",
nh.code as "ma_huyen",nh.name as "huyen",
nn.code as "pos_code",nn.name as "pos",
   pp.name_template as "sp",
   pc_nhom_nganh_hang.name as "nganh_hang",
   pc_nhom_hang.name as "nhom_hang",
   pc_nhom_sp.name as "nhom_sp",
   rp.name as "provider",
   nn.id as "net_id",
   pp.id as "id_sp",
   
                       po.name as "dvt", 
                        ppi.price_surcharge as "price",
                        sum(sq.qty) as "quant"
                  from product_template  pt
                  inner join product_product pp on pt.id=pp.product_tmpl_id
                  inner join product_uom po on po.id =pt.uom_id
                  inner join product_category pc_nhom_sp on pc_nhom_sp.id =pt.categ_id
       inner join product_category pc_nhom_hang on pc_nhom_sp.parent_id =pc_nhom_hang.id
       inner join product_category pc_nhom_nganh_hang on pc_nhom_hang.parent_id =pc_nhom_nganh_hang.id
       inner join product_brand pb on pb.id =pt.product_brand_id
       inner join res_partner rp on rp.id =pb.partner_id
                  inner join product_pricelist_item ppi on ppi.product_id =pp.id
                  inner join stock_quant sq on sq.product_id=pp.id
                  inner join stock_location sl on sl.id=sq.location_id
                  inner join stock_warehouse sw on sw.lot_stock_id=sl.id
                  inner join network_node nn on nn.id =sw.network_id
                  inner join network_node nh on nh.id =nn.parent_id
                  inner join network_node nt on  nt.id =nh.parent_id
       join network_node nt_btcom on  nt_btcom .id =nt.parent_id

       where nn.id in (%s)

                   group by  pp.id ,pp.name_template ,pp.ean13 ,po.id , 
                   ppi.price_surcharge ,sw.network_id ,sw.code,pc_nhom_sp.name,pc_nhom_hang.name,pc_nhom_nganh_hang,pc_nhom_nganh_hang.name,rp.name,
                   nt_btcom.code,nt_btcom.name,nt.code,nt.name,nh.code,nh.name,nn.code,nn.name, nn.id"""