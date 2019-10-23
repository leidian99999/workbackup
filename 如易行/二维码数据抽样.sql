
SELECT t.*,
       b.entry_station_name,
       b.exit_station_name,
       b.userid,
       b.ticket_price,
       b.actual_price,
       b.business_date_str,
       b.exit_date_time_str,
       b.entry_date_time_str
FROM
  (SELECT a.*
   FROM
     (SELECT card_num,
             credit_point_start_date,
             credit_point,
             trans_count,
             actual_payment,
             user_id,
             province,
             city,
             gender,
             age,
             phonebrand,
             phonecarrier,
             phoneregion,
             paymentmethod,
             firstentry
      FROM icr_credit_point_ledger
      WHERE substr(credit_point_start_date,1,6) = "201904"  --月份修改
        AND ticket_type = "11"
      ORDER BY rand()) AS a LIMIT 1000) AS t --选取随机样本数
LEFT JOIN icr_user_trans AS b ON t.user_id = b.userid
WHERE b.ticket_type = "11"
  AND b.product_type = "01"
  AND b.business_date_str BETWEEN "20190401" AND "20190402" --日期修改
ORDER BY b.userid,
         b.business_date_str,
         b.entry_date_time_str,
         b.exit_date_time_str