sap_columns_to_master_columns = {'Планирующий завод':'be_code', 'Единица оборудования': 'eo_code', 'Название технического объекта':'eo_description', 'Техническое место': 'teh_mesto','Поле сортировки':'gar_no', "ДатВвода в эксплуат.":'operation_start_date', 'Системный статус': 'sap_system_status', 'Пользовательский статус': 'sap_user_status', 'План. срок вывода об.из экспл.': 'sap_planned_finish_operation_date', 'Марка заводская': 'sap_model_name', 'Гаражный номер': 'sap_gar_no','Изготовитель ПроизводУстановки': 'sap_maker'}

be_data_columns_to_master_columns = {"№пп": "be_eo_data_row_no", "ЕО SAP": "eo_code", "Гаражный №": "gar_no", 'Дата ввода в экспл.(полностью включая день) ': 'reported_operation_start_date', 'Дата ввода в экспл': 'reported_operation_start_date', 'Плановая дата вывода из эксплуат': 'reported_operation_finish_date', 'Статус эксплуатации': 'operation_status', 'Дата статуса эксплуатации': 'operation_status_date', 'Удаление записи':'delete_eo_record'}

sap_system_status_ban_list = ['МТКУ НЕАК УСТН', 'МТКУ ПВЕО', 'МТКУ УСТН']
sap_user_status_ban_list = ['КОНС СИНХ', 'КОНС', 'ВРНД НПВЭ СИНХ']
sap_user_status_cons_status_list = ['КОНС СИНХ', 'КОНС']
be_data_cons_status_list = ["Консервация", "консервация"]