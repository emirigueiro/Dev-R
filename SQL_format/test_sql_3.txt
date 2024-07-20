WITH tmp_1 AS
#1er nivel de agregación para la construcción de metricas de BU
#______________________________________________________________________________________________________________________________________
(
SELECT SUM(IFNULL(CASE WHEN reg_uni_adc = 1 THEN hsColacion_adicionales * 86400 END,0)/3600)                                                                                                               AS Colacion,
SUM((IFNULL(case when reg_uni_adc=1 and idTipoHorario=1 then  jornadapactada_adicionales * 86400 end,0)/3600) - (IFNULL(CASE WHEN reg_uni_adc = 1 THEN hsColacion_adicionales * 86400 END,0)/3600)) AS Teoricas_Menos_Colacion,
SUM(IFNULL(case when reg_uni_adc=1 and valorNegativoRecupero_adicionales=false and ontraining = False then hsRecupero_adicionales * 86400 end,0)/3600)                                              AS Recuperos, #Hs_Recuperos_Realizados
SUM(IFNULL(case when reg_uni_aus=1 and tho_nombre='Recupero de horas' and ontraining = False then  (Hs_No_Trabajadas * 24)  end,0))                                                                 AS Hs_Recuperos_No_Realizados,
SUM((IFNULL(CASE WHEN reg_uni_adc = 1 and ontraining = False THEN hsExtra_adicionales * 86400 END,0))/3600)                                                                                         AS Horas_extra, #Hs_Adicionales_Realizadas
SUM((IFNULL(CASE WHEN reg_uni_aus = 1 and tho_nombre='Horas Adicionales'  and ontraining = False THEN  (Hs_No_Trabajadas * 24)  END,0)))                                                            AS Hs_Adicionales_No_Realizadas,
SUM((IFNULL(case when reg_uni_adc = 1 and tho_nombre='Autorizado por supervisor' and ontraining = False then  (jornadapactada_adicionales * 86400)/3600 end,0)))                                    AS Autorizado_por_Sup,
SUM((IFNULL(case when reg_uni_adc = 1 and idTipoHorario=1 and ontraining = False  then (jornadapactada_adicionales * 86400)/3600 end,0)))                                                           AS Jornada_Pactada,                          
SUM(case when reg_uni_aus=1 and ontraining = False then (IFNULL(case when reg_uni_aus=1 then  Hs_No_Trabajadas * 86400 end,0)/3600) end)                                                            AS Ausentismo_no_Gestionable,
SUM(CASE WHEN pago = true AND reg_uni_aus = 1 and ontraining = False THEN (IFNULL(case when reg_uni_aus=1 then  Hs_No_Trabajadas * 86400 end,0)/3600) END)                                          AS Ausentismo_No_Gestionable_Pago,
SUM(CASE WHEN pago = false AND reg_uni_aus = 1 and ontraining = False THEN (IFNULL(case when reg_uni_aus=1 then Hs_No_Trabajadas * 86400 end,0)/3600) END)                                          AS Ausentismo_No_Gestionable_No_Pago,
SUM(case when reg_uni_aus=1 and ausentismo=true and ontraining = False then (IFNULL(case when reg_uni_aus=1 then  Hs_No_Trabajadas * 86400 end,0)/3600) end)                                        AS Ausentismo_Gestionable,
SUM(case when reg_uni_aus=1 and pago = true and ausentismo=true and ontraining = False then (IFNULL(case when reg_uni_aus=1 then  Hs_No_Trabajadas * 86400 end,0)/3600) end)                        AS Ausentismo_Gestionable_Pago,
SUM(case when reg_uni_aus=1 and pago = false and ausentismo=true and ontraining = False then (IFNULL(case when reg_uni_aus=1 then  Hs_No_Trabajadas * 86400 end,0)/3600) end)                       AS Ausentismo_Gestionable_No_Pago,
SUM(IFNULL(CASE WHEN Facturable  = 'SI' AND reg_uni_real = 1 and ontraining = False THEN ((Tiempo_en_estado_real)*86400/3600) END,0))                                                               AS Logueo_Facturable,
SUM((ifnull(CASE WHEN Facturable  = 'NO' AND reg_uni_real = 1 and ontraining = False THEN Tiempo_en_estado_real * 86400 END,0))/3600)                                                               AS Logueo_No_Facturable,
SUM((ifnull(CASE WHEN Deslogueo_Teletrabajo>0 AND reg_uni_des = 1 and ontraining = False  THEN Deslogueo_Teletrabajo* 86400 END,0))/3600)                                                           AS Deslogueo_Teletrabajo,
SUM((ifnull(CASE WHEN Deslogueo_Aux_genesis>0 AND reg_uni_des = 1 and ontraining = False  THEN Deslogueo_Aux_genesis * 86400 END,0))/3600)                                                          AS Deslogueo_Aux_Genesis,
SUM((IFNULL(CASE WHEN Deslogueo_No_Facturable>0 AND reg_uni_des = 1 and ontraining = False  THEN Deslogueo_No_Facturable *86400 END,0))/3600)                                                       AS Deslogueo_No_Facturable,    
SUM(IFNULL(CASE WHEN Deslogueo_Facturable > 0 AND reg_uni_des = 1 and ontraining = False THEN ((Deslogueo_Facturable)*86400/3600) END,0))                                                           AS Deslogueo_Facturable,
SUM(IFNULL(case when reg_uni_adc=1 and valorNegativoRecupero_adicionales=false and ontraining = True then hsRecupero_adicionales * 86400 end,0)/3600)                                               AS Recuperos_Capa,
SUM((IFNULL(CASE WHEN reg_uni_adc = 1 and ontraining = True THEN hsExtra_adicionales * 86400 END,0))/3600)                                                                                          AS Horas_extra_Capa,    
SUM(IFNULL(case when reg_uni_adc=1 and idTipoHorario=1 AND Ontraining = true then  jornadapactada_adicionales * 86400 end,0)/3600)                                                                  AS Capacitacion_No_Facturable_1,
SUM(IFNULL(case when 0 = 0 then  0 end,0))                                                                                                                                                          AS Capacitacion_Facturable, #En construcción       
SUM(IFNULL(CASE WHEN tno_id = 5 AND eno_id IN (3,1)  AND reg_uni_aus = 1 and ontraining = False THEN (Hs_No_Trabajadas * 24)  END,0))                                                               AS Inasistencias_injustificadas,
SUM(IFNULL(CASE WHEN tno_id = 5 AND pago = false AND reg_uni_aus = 1 and ontraining = False and eno_id = 2 THEN (Hs_No_Trabajadas * 24)  END,0))                                                    AS Inasistencias_No_Pagas,
SUM(IFNULL(CASE WHEN tno_id = 5 AND eno_id=1 AND reg_uni_aus = 1  and ontraining = False THEN (Hs_No_Trabajadas * 24)  END,0))                                                                      AS Inasistencias_Pendientes,
SUM(IFNULL(CASE WHEN tno_id = 5 AND pago = true AND reg_uni_aus = 1 and ontraining = False THEN (Hs_No_Trabajadas * 24)  END,0))                                                                    AS Inasistencias_Pagas_1,
SUM(IFNULL(CASE WHEN tno_id = 2 AND pago = false AND reg_uni_aus = 1 and ontraining = False THEN (Hs_No_Trabajadas * 24)  END,0))                                                                   AS Llegadastarde_no_pagas,
SUM(IFNULL(CASE WHEN tno_id = 2 AND pago = true AND reg_uni_aus = 1 and ontraining = False THEN (Hs_No_Trabajadas * 24)  END,0))                                                                    AS Llegadastarde_pagas_1,
SUM(IFNULL(CASE WHEN tno_id = 3 AND pago = false AND reg_uni_aus = 1 and ontraining = False THEN (Hs_No_Trabajadas * 24)  END,0))                                                                   AS Retiroantes_no_pagas,
SUM(IFNULL(CASE WHEN tno_id = 3 AND pago = true AND reg_uni_aus = 1 and ontraining = False THEN (Hs_No_Trabajadas * 24)  END,0))                                                                    AS Retiroantes_pagas_1,
SUM(IFNULL(CASE WHEN   reg_uni_adc = 1 and valorNegativoRecupero_adicionales = true AND Ontraining = false then Hs_No_Trabajadas*24 END,0))                                                         AS Ausencias_recuperos,
SUM(IFNULL(CASE WHEN   tno_id = 5 AND pago = true AND reg_uni_adc = 1 and valorNegativoRecupero_adicionales = true AND Ontraining = false then Hs_No_Trabajadas*24 END,0))                          AS Ausencias_recuperos_INASISTENCIAS,
SUM(IFNULL(CASE WHEN   tno_id = 2 AND pago = true AND reg_uni_adc = 1 and valorNegativoRecupero_adicionales = true AND Ontraining = false then Hs_No_Trabajadas*24 END,0))                          AS Ausencias_recuperos_LLEGADAS_TARDE,
SUM(IFNULL(CASE WHEN   tno_id = 3 AND pago = true AND reg_uni_adc = 1 and valorNegativoRecupero_adicionales = true AND Ontraining = false then Hs_No_Trabajadas*24 END,0))                          AS Ausencias_recuperos_RETIROS_ANTES,    
SUM(IFNULL(case when Break_='SI' and reg_uni_real = 1 and Facturable = 'NO' AND Ontraining = false then (Tiempo_en_estado_real * 86400)/3600 end,0))                                                AS Break_no_facturable,
SUM(IFNULL(case when Break_='SI' and reg_uni_real = 1 and Facturable = 'SI' AND Ontraining = false then (Tiempo_en_estado_real * 86400)/3600 end,0))                                                AS Break_facturable, idpais_nomina, Pais_nomina, Ratios, UPPER(Cuenta_nomina) AS Cuenta_nomina, idcuenta,  CONCAT(CAST(EXTRACT(YEAR FROM FechaRegistro) AS STRING), '-', LPAD(CAST(EXTRACT(MONTH FROM FechaRegistro) AS STRING), 2, '0')) AS anio_mes,

       FechaRegistro,                

FROM `dm-tmi-prd-39631.tmi_prd.tmi_bu` WHERE Ratios = 'Directos' GROUP BY idpais_nomina, Pais_nomina, Cuenta_nomina, idcuenta, anio_mes, Ratios, FechaRegistro
)
#2do nivel de agregación para la construcción de metricas de BU (exclusivo para Capacitacion_no_facturable)
#______________________________________________________________________________________________________________________________________
, tmp_0 AS (SELECT   tmp_1.* , COALESCE(Capacitacion_No_Facturable_1 + Recuperos_Capa + Horas_extra_Capa,0)                                                                                                              AS Capacitacion_No_Facturable
FROM tmp_1)
#3er nivel de agregación para la construcción de metricas de BU
#______________________________________________________________________________________________________________________________________
, tmp_2 AS
(
SELECT  tmp_0.*, COALESCE(Jornada_Pactada + Autorizado_por_Sup ,0)                                                                                                                                          AS Teoricas,

  COALESCE(Horas_extra + Autorizado_por_Sup + Jornada_Pactada + Recuperos + Capacitacion_No_Facturable + Capacitacion_Facturable,0)                                                                AS Horas_Totales,

  COALESCE(Horas_extra + Autorizado_por_Sup + Jornada_Pactada + Recuperos ,0)                                                                                                                      AS Horas_Totales_Sin_Capacitacion,

  COALESCE((IFNULL(Horas_extra,0) + IFNULL(Autorizado_por_Sup,0) + IFNULL(Jornada_Pactada,0) + IFNULL(Recuperos,0) + IFNULL(Capacitacion_No_Facturable,0) + IFNULL(Capacitacion_Facturable,0)
            - IFNULL(Colacion,0)),
           (IFNULL(Horas_extra,0) + IFNULL(Autorizado_por_Sup,0) + IFNULL(Jornada_Pactada,0) + IFNULL(Recuperos,0) + IFNULL(Capacitacion_No_Facturable,0) + IFNULL(Capacitacion_Facturable,0)))    AS Horas_Totales_sin_Colacion,

  COALESCE(Logueo_Facturable + Deslogueo_Facturable + Capacitacion_Facturable,0)                                                                                                                   AS Horas_Produccion,   


  COALESCE((IFNULL(Horas_extra,0) + IFNULL(Autorizado_por_Sup,0) + IFNULL(Jornada_Pactada,0) + IFNULL(Recuperos,0) + IFNULL(Capacitacion_No_Facturable,0) + IFNULL(Capacitacion_Facturable,0))
            - IFNULL(Ausentismo_no_Gestionable,0),
           (IFNULL(Horas_extra,0) + IFNULL(Autorizado_por_Sup,0) + IFNULL(Jornada_Pactada,0) + IFNULL(Recuperos,0) + IFNULL(Capacitacion_No_Facturable,0) + IFNULL(Capacitacion_Facturable,0)))    AS Horas_Presentes,        

   
  COALESCE(IFNULL(Logueo_No_Facturable,0) - IFNULL(Break_no_facturable,0),IFNULL(Logueo_No_Facturable,0))                                                                                          AS Logueo_No_Facturable_sin_Break,

  COALESCE(Inasistencias_Pagas_1 - Ausencias_recuperos_INASISTENCIAS, Inasistencias_Pagas_1)                                                                                                       AS Inasistencias_Pagas,

  COALESCE(Llegadastarde_pagas_1 - Ausencias_recuperos_LLEGADAS_TARDE, Llegadastarde_pagas_1)                                                                                                      AS Llegadastarde_pagas,

  COALESCE(Retiroantes_pagas_1 - Ausencias_recuperos_RETIROS_ANTES, Retiroantes_pagas_1)                                                                                                           AS Retiroantes_pagas
   
FROM tmp_0
)
#4to nivel de agregación para la construcción de metricas de BU
#______________________________________________________________________________________________________________________________________
, bu AS
(
SELECT  tmp_2.*,      
  COALESCE((IFNULL(Teoricas, 0) + IFNULL(Horas_extra, 0) + IFNULL(Capacitacion_No_Facturable, 0) + IFNULL(Capacitacion_Facturable, 0) + IFNULL(Recuperos, 0))
            - (IFNULL(Ausentismo_No_Gestionable_No_Pago, 0) + IFNULL(Break_no_facturable, 0) + IFNULL(Recuperos, 0)),
           (IFNULL(Teoricas, 0) + IFNULL(Horas_extra, 0) + IFNULL(Capacitacion_No_Facturable, 0) + IFNULL(Capacitacion_Facturable, 0) + IFNULL(Recuperos, 0)))                                     AS Horas_Pagadas,


  COALESCE((Logueo_Facturable + Deslogueo_Facturable + Capacitacion_Facturable +  Deslogueo_No_Facturable + Logueo_No_Facturable_sin_Break + Deslogueo_Aux_Genesis + Deslogueo_Teletrabajo
             + Capacitacion_No_Facturable + Break_no_facturable)
             - (Horas_Presentes),                                      
           (Logueo_Facturable + Deslogueo_Facturable + Capacitacion_Facturable +  Deslogueo_No_Facturable + Logueo_No_Facturable_sin_Break + Deslogueo_Aux_Genesis + Deslogueo_Teletrabajo
             + Capacitacion_No_Facturable + Break_no_facturable))                                                                                                                                  AS Horas_Impresicion,    

  COALESCE(Deslogueo_No_Facturable + Deslogueo_Aux_Genesis + Deslogueo_Teletrabajo + Logueo_No_Facturable_sin_Break + Capacitacion_No_Facturable + Break_no_facturable, 0)                         AS Improductividades_Agente,
     
FROM tmp_2

WHERE Ratios = 'Directos' AND Cuenta_nomina is not null
)

#Select final
#______________________________________________________________________________________________________________________________________
SELECT
       bu.idpais_nomina,       bu.Pais_nomina,       bu.idcuenta,       bu.Cuenta_nomina,       bu.anio_mes,       bu.FechaRegistro,
           
       #Indicadores_BU
       COALESCE(bu.Colacion,0)   AS Colacion,
       COALESCE(bu.Teoricas,0)                                                        AS Teoricas,
       COALESCE(bu.Teoricas_Menos_Colacion,0)      AS Teoricas_Menos_Colacion,
       COALESCE(bu.Horas_Totales,0)                                                   AS Horas_Totales,
       COALESCE(bu.Horas_Totales_Sin_Capacitacion,0)   AS Horas_Totales_Sin_Capacitacion,
       COALESCE(bu.Horas_Totales_sin_Colacion,0)                                      AS Horas_Totales_sin_Colacion,
       COALESCE(bu.Horas_Produccion,0)                                                AS Horas_Produccion,
       COALESCE(bu.Horas_Presentes,0)                AS Horas_Presentes,
       COALESCE(bu.Horas_Pagadas,0)                                                   AS Horas_Pagadas,
       COALESCE(bu.Recuperos,0)                                                       AS Recuperos,
       COALESCE(bu.Hs_Recuperos_No_Realizados,0)                                      AS Hs_Recuperos_No_Realizados,
       COALESCE(bu.Horas_extra,0)                                                     AS Horas_extra,
       COALESCE(bu.Hs_Adicionales_No_Realizadas,0)                                    AS Hs_Adicionales_No_Realizadas,
       COALESCE(bu.Autorizado_por_Sup,0)                                              AS Autorizado_por_Sup,
       COALESCE(bu.Jornada_Pactada,0)                                                 AS Jornada_Pactada,
       COALESCE(bu.Ausentismo_No_Gestionable,0)                                       AS Ausentismo_No_Gestionable,
       COALESCE(bu.Ausentismo_No_Gestionable_Pago,0)                                  AS Ausentismo_No_Gestionable_Pago,
       COALESCE(bu.Ausentismo_No_Gestionable_No_Pago,0)                               AS Ausentismo_No_Gestionable_No_Pago,
       COALESCE(bu.Ausentismo_Gestionable,0)                                          AS Ausentismo_Gestionable,
       COALESCE(bu.Ausentismo_Gestionable_Pago,0)                                     AS Ausentismo_Gestionable_Pago,
       COALESCE(bu.Ausentismo_Gestionable_No_Pago,0)                                  AS Ausentismo_Gestionable_No_Pago,
       COALESCE(bu.Logueo_Facturable,0)                                               AS Logueo_Facturable,
       COALESCE(bu.Logueo_No_Facturable,0)                                            AS Logueo_No_Facturable,
       COALESCE(bu.Logueo_No_Facturable_sin_Break,0)                                  AS Logueo_No_Facturable_sin_Break,
       COALESCE(bu.Deslogueo_Teletrabajo,0)                                           AS Deslogueo_No_Facturable_Teletrabajo,
       COALESCE(bu.Deslogueo_Aux_Genesis,0)                                           AS Deslogueo_No_Facturable_Aux_Genesis,
      0                                                                               AS Deslogueo_Facturable_Teletrabajo,    #En construcción
      0                                                                               AS Deslogueo_Facturable_Aux_Genesis,    #En construcción
       COALESCE(bu.Deslogueo_Facturable,0)                                            AS Deslogueo_Facturable,
       COALESCE(bu.Deslogueo_No_Facturable,0)                                         AS Deslogueo_No_Facturable,
      -- COALESCE(bu.Logueo_No_Facturable,0)                                          AS Horas_No_Facturable,          
       COALESCE(bu.Capacitacion_No_Facturable,0)                                      AS Capacitacion_No_Facturable,
       COALESCE(bu.Capacitacion_Facturable,0)                                         AS Capacitacion_Facturable,             #En construcción
       COALESCE(bu.Inasistencias_injustificadas,0)                                    AS Inasistencias_injustificadas,
       COALESCE(bu.Inasistencias_No_Pagas,0)                                          AS Inasistencias_No_Pagas,
       COALESCE(bu.Inasistencias_Pendientes,0)                                        AS Inasistencias_Pendientes,
       COALESCE(bu.Inasistencias_Pagas,0)                                             AS Inasistencias_Pagas,
       COALESCE(bu.Llegadastarde_no_pagas,0)                                          AS Llegadastarde_no_pagas,
       COALESCE(bu.Llegadastarde_pagas,0)                                             AS Llegadastarde_pagas,
       COALESCE(bu.Retiroantes_no_pagas,0)                                            AS Retiroantes_no_pagas,
       COALESCE(bu.Retiroantes_pagas,0)                                               AS Retiroantes_pagas,
       COALESCE(bu.Ausencias_recuperos,0)                                             AS Ausencias_recuperos,
       COALESCE(bu.Improductividades_Agente,0)                                        AS Improductividades_Agente,
       COALESCE(bu.Break_no_facturable,0)                                             AS Break_no_facturable,
       COALESCE(bu.Break_facturable,0)                                                AS Break_facturable,
       COALESCE(bu.Horas_Impresicion,0)                                               AS Horas_Impresicion,
       COALESCE(bu.Horas_Produccion)                                                  AS Total_Facturado,

FROM bu

WHERE bu.FechaRegistro NOT IN (CURRENT_DATE(), DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY)) --> Debido al lag en la carga de información, los datos del día actual y el anterior no son representativos. 
