# -*- coding: utf-8 -*- 


import wx
import wx.xrc

import os.path


import input_output.io as io
import clustering.k_means.k_means_plt as k_means
import classification.Stochastic_Gradient_Descent.sgd


###########################################################################
## Class MainWindow
###########################################################################

class MainWindow(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Data Mining", pos=wx.DefaultPosition,
                          size=wx.Size(330, 510), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(330, 510), wx.Size(330, 510))

        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # region Меню

        self.m_menubar1 = wx.MenuBar(0)
        self.menu = wx.Menu()

        # region Меню/Классификация
        self.menu_classification = wx.Menu()

        self.menu_classification_Support_vector_machines = wx.MenuItem(self.menu_classification, wx.ID_ANY,
                                                                       u"Support vector machines", wx.EmptyString,
                                                                       wx.ITEM_NORMAL)
        self.menu_classification.Append(self.menu_classification_Support_vector_machines)
        self.menu_classification_Stochastic_gradient_descent = wx.MenuItem(self.menu_classification, wx.ID_ANY,
                                                                           u"Stochastic gradient descent",
                                                                           wx.EmptyString,
                                                                           wx.ITEM_NORMAL)
        self.menu_classification.Append(self.menu_classification_Stochastic_gradient_descent)
        self.menu_classification_Nearest_Neighbors = wx.MenuItem(self.menu_classification, wx.ID_ANY,
                                                                 u"Nearest Neighbors", wx.EmptyString,
                                                                 wx.ITEM_NORMAL)
        self.menu_classification.Append(self.menu_classification_Nearest_Neighbors)
        self.menu_classification_Gaussian_Processes = wx.MenuItem(self.menu_classification, wx.ID_ANY,
                                                                  u"Gaussian Processes", wx.EmptyString,
                                                                  wx.ITEM_NORMAL)
        self.menu_classification.Append(self.menu_classification_Gaussian_Processes)
        self.menu_classification_Decision_trees = wx.MenuItem(self.menu_classification, wx.ID_ANY, u"Decision trees",
                                                              wx.EmptyString,
                                                              wx.ITEM_NORMAL)
        self.menu_classification.Append(self.menu_classification_Decision_trees)
        self.menu_classification_naiv_bais = wx.MenuItem(self.menu_classification, wx.ID_ANY,
                                                         u"Наивная байесовская классификация", wx.EmptyString,
                                                         wx.ITEM_NORMAL)
        self.menu_classification.Append(self.menu_classification_naiv_bais)
        self.menu_classification_kmeanes = wx.MenuItem(self.menu_classification, wx.ID_ANY,
                                                       u"Алгоритм k-ближайших соседей (кф)", wx.EmptyString,
                                                       wx.ITEM_NORMAL)
        self.menu_classification.Append(self.menu_classification_kmeanes)
        self.menu_classification_less_sqad = wx.MenuItem(self.menu_classification, wx.ID_ANY,
                                                         u"Алгоритм наименьших квадратов", wx.EmptyString,
                                                         wx.ITEM_NORMAL)
        self.menu_classification.Append(self.menu_classification_less_sqad)
        self.menu_classification_rokkio = wx.MenuItem(self.menu_classification, wx.ID_ANY, u"Алгоритм Роккио",
                                                      wx.EmptyString,
                                                      wx.ITEM_NORMAL)
        self.menu_classification.Append(self.menu_classification_rokkio)
        self.menu_classification_vectors = wx.MenuItem(self.menu_classification, wx.ID_ANY,
                                                       u"Алгоритм опорных векторов", wx.EmptyString,
                                                       wx.ITEM_NORMAL)
        self.menu_classification.Append(self.menu_classification_vectors)
        self.menu.AppendSubMenu(self.menu_classification, u"Классификация")
        # endregion

        # region Меню/Кластеризация
        self.menu_clusterization = wx.Menu()

        self.menu_clusterization_kmeans = wx.MenuItem(self.menu_clusterization, wx.ID_ANY, u"K-means", wx.EmptyString,
                                                      wx.ITEM_NORMAL)
        self.menu_clusterization.Append(self.menu_clusterization_kmeans)
        self.menu_clusterization_id3 = wx.MenuItem(self.menu_clusterization, wx.ID_ANY, u"ID3", wx.EmptyString,
                                                   wx.ITEM_NORMAL)
        self.menu_clusterization.Append(self.menu_clusterization_id3)
        self.menu_clusterization_Affinity_Propagation = wx.MenuItem(self.menu_clusterization, wx.ID_ANY,
                                                                    u"Affinity Propagation", wx.EmptyString,
                                                                    wx.ITEM_NORMAL)
        self.menu_clusterization.Append(self.menu_clusterization_Affinity_Propagation)
        self.menu_clusterization_Birch = wx.MenuItem(self.menu_clusterization, wx.ID_ANY, u"Birch", wx.EmptyString,
                                                     wx.ITEM_NORMAL)
        self.menu_clusterization.Append(self.menu_clusterization_Birch)
        self.menu_clusterization_Mean_Shift = wx.MenuItem(self.menu_clusterization, wx.ID_ANY, u"Mean Shift",
                                                          wx.EmptyString,
                                                          wx.ITEM_NORMAL)
        self.menu_clusterization.Append(self.menu_clusterization_Mean_Shift)
        self.menu_clusterization_Perfomance_evalution = wx.MenuItem(self.menu_clusterization, wx.ID_ANY,
                                                                    u"Perfomance evalution", wx.EmptyString,
                                                                    wx.ITEM_NORMAL)
        self.menu_clusterization.Append(self.menu_clusterization_Perfomance_evalution)
        self.menu_clusterization_Hierarchical_clustering = wx.MenuItem(self.menu_clusterization, wx.ID_ANY,
                                                                       u"Hierarchical clustering", wx.EmptyString,
                                                                       wx.ITEM_NORMAL)
        self.menu_clusterization.Append(self.menu_clusterization_Hierarchical_clustering)
        self.menu_clusterization_Adjusted_Rand_index = wx.MenuItem(self.menu_clusterization, wx.ID_ANY,
                                                                   u"Adjusted Rand index", wx.EmptyString,
                                                                   wx.ITEM_NORMAL)
        self.menu_clusterization.Append(self.menu_clusterization_Adjusted_Rand_index)
        self.menu_clusterization_DBSCAN = wx.MenuItem(self.menu_clusterization, wx.ID_ANY, u"DBSCAN", wx.EmptyString,
                                                      wx.ITEM_NORMAL)
        self.menu_clusterization.Append(self.menu_clusterization_DBSCAN)
        self.menu_clusterization_MutualInformationbasedscore = wx.MenuItem(self.menu_clusterization, wx.ID_ANY,
                                                                           u"Mutual Information based score",
                                                                           wx.EmptyString,
                                                                           wx.ITEM_NORMAL)
        self.menu_clusterization.Append(self.menu_clusterization_MutualInformationbasedscore)
        self.menu_clusterization_Silhouette_Coefficient = wx.MenuItem(self.menu_clusterization, wx.ID_ANY,
                                                                      u"Silhouette Coefficient", wx.EmptyString,
                                                                      wx.ITEM_NORMAL)
        self.menu_clusterization.Append(self.menu_clusterization_Silhouette_Coefficient)
        self.menu_clusterization_Fowlkes_Mallows_scores = wx.MenuItem(self.menu_clusterization, wx.ID_ANY,
                                                                      u"Fowlkes-Mallows scores", wx.EmptyString,
                                                                      wx.ITEM_NORMAL)
        self.menu_clusterization.Append(self.menu_clusterization_Fowlkes_Mallows_scores)
        self.menu_clusterization_V_measure = wx.MenuItem(self.menu_clusterization, wx.ID_ANY, u"V-measure",
                                                         wx.EmptyString,
                                                         wx.ITEM_NORMAL)
        self.menu_clusterization.Append(self.menu_clusterization_V_measure)
        self.menu_clusterization_Spectral_clustering = wx.MenuItem(self.menu_clusterization, wx.ID_ANY,
                                                                   u"Spectral clustering", wx.EmptyString,
                                                                   wx.ITEM_NORMAL)
        self.menu_clusterization.Append(self.menu_clusterization_Spectral_clustering)
        self.menu.AppendSubMenu(self.menu_clusterization, u"Кластеризация")
        # endregion

        # region Меню/Асоциативные правила
        self.menu_asociative_rules = wx.Menu()
        self.menu_asociative_rules_apriori = wx.MenuItem(self.menu_asociative_rules, wx.ID_ANY, u"Apriori",
                                                         wx.EmptyString,
                                                         wx.ITEM_NORMAL)
        self.menu_asociative_rules.Append(self.menu_asociative_rules_apriori)
        self.menu_asociative_rules_aprioriTID = wx.MenuItem(self.menu_asociative_rules, wx.ID_ANY, u"AprioriTID",
                                                            wx.EmptyString,
                                                            wx.ITEM_NORMAL)
        self.menu_asociative_rules.Append(self.menu_asociative_rules_aprioriTID)
        self.menu_asociative_rules_aprioriHybrid = wx.MenuItem(self.menu_asociative_rules, wx.ID_ANY, u"AprioriHybrid",
                                                               wx.EmptyString,
                                                               wx.ITEM_NORMAL)
        self.menu_asociative_rules.Append(self.menu_asociative_rules_aprioriHybrid)
        self.menu_asociative_rules_DHP = wx.MenuItem(self.menu_asociative_rules, wx.ID_ANY, u"DHP",
                                                     wx.EmptyString,
                                                     wx.ITEM_NORMAL)
        self.menu_asociative_rules.Append(self.menu_asociative_rules_DHP)
        self.menu_asociative_rules_PARTITION = wx.MenuItem(self.menu_asociative_rules, wx.ID_ANY, u"PARTITION",
                                                           wx.EmptyString,
                                                           wx.ITEM_NORMAL)
        self.menu_asociative_rules.Append(self.menu_asociative_rules_PARTITION)

        self.menu.AppendSubMenu(self.menu_asociative_rules, u"Поиск ассоциативных правил")
        # endregion

        self.m_menubar1.Append(self.menu, u"Задача")

        self.SetMenuBar(self.m_menubar1)
        # endregion

        # region Рабочая область
        self.lable_task = wx.StaticText(self, wx.ID_ANY, u"Задача: Не выбрана", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lable_task.Wrap(-1)
        self.lable_task.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        gbSizer1.Add(self.lable_task, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.lable_algo = wx.StaticText(self, wx.ID_ANY, u"Алгоритм: Не выбран", wx.DefaultPosition, wx.DefaultSize, 0)
        self.lable_algo.Wrap(-1)
        self.lable_algo.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        gbSizer1.Add(self.lable_algo, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.lable_choice_data = wx.StaticText(self, wx.ID_ANY, u"Использовать данные из:", wx.DefaultPosition,
                                               wx.Size(-1, -1), wx.ALIGN_CENTRE)
        self.lable_choice_data.Wrap(-1)
        self.lable_choice_data.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))
        self.lable_choice_data.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))

        gbSizer1.Add(self.lable_choice_data, wx.GBPosition(3, 1), wx.GBSpan(1, 9), wx.ALL | wx.EXPAND, 5)

        self.radioBtn_data_file = wx.RadioButton(self, wx.ID_ANY, u"Файла", wx.DefaultPosition, wx.DefaultSize, 0)
        self.radioBtn_data_file.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL,
                    False, wx.EmptyString))

        gbSizer1.Add(self.radioBtn_data_file, wx.GBPosition(5, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.data_file_picker = wx.FilePickerCtrl(self, wx.ID_ANY, u"Укажите путь к файлу", u"Выберите файл",
                                                  u"data (*.csv,*.txt)|*.csv;*.txt", wx.DefaultPosition,
                                                  wx.DefaultSize, wx.FLP_DEFAULT_STYLE | wx.FLP_SMALL)
        gbSizer1.Add(self.data_file_picker, wx.GBPosition(6, 1), wx.GBSpan(1, 9), wx.ALL | wx.EXPAND, 5)
        self.data_file_picker.Enable(False)

        self.radioBtn_link = wx.RadioButton(self, wx.ID_ANY, u"Интернета (URL)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.radioBtn_link.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL,
                    False, wx.EmptyString))

        gbSizer1.Add(self.radioBtn_link, wx.GBPosition(7, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.data_link = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_AUTO_URL)
        gbSizer1.Add(self.data_link, wx.GBPosition(8, 1), wx.GBSpan(1, 9), wx.ALL | wx.EXPAND, 5)
        self.data_link.Enable(False)

        self.radioBtn_random = wx.RadioButton(self, wx.ID_ANY, u"Случайные", wx.DefaultPosition, wx.DefaultSize, 0)
        self.radioBtn_random.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL,
                    False, wx.EmptyString))

        gbSizer1.Add(self.radioBtn_random, wx.GBPosition(9, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.lable_test_data = wx.StaticText(self, wx.ID_ANY, u"Файл проверочных данных:", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.lable_test_data.Wrap(-1)
        self.lable_test_data.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        gbSizer1.Add(self.lable_test_data, wx.GBPosition(12, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.algo_state = wx.StaticText(self, wx.ID_ANY, u"empty", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.algo_state.Wrap(-1)
        self.algo_state.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        gbSizer1.Add(self.algo_state, wx.GBPosition(20, 1), wx.GBSpan(20, 1), wx.ALL, 5)

        self.data_test_file = wx.FilePickerCtrl(self, wx.ID_ANY, u"Укажите путь к файлу", u"Выберите файл",
                                                u"data (*.csv,*.txt,*.xls)|*.csv;*.txt;*.xls", wx.DefaultPosition,
                                                wx.DefaultSize, wx.FLP_DEFAULT_STYLE | wx.FLP_SMALL)
        gbSizer1.Add(self.data_test_file, wx.GBPosition(13, 1), wx.GBSpan(1, 9), wx.ALL | wx.EXPAND, 5)

        self.run_algo = wx.Button(self, wx.ID_ANY, u"Выполнить", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.run_algo, wx.GBPosition(15, 1), wx.GBSpan(4, 9), wx.ALL | wx.EXPAND, 5)

        self.SetSizer(gbSizer1)
        self.Layout()

        self.Centre(wx.BOTH)
        # endregion



        self.radioBtn_data_file.Bind(wx.EVT_RADIOBUTTON, self.rdn_file)
        self.radioBtn_link.Bind(wx.EVT_RADIOBUTTON, self.rdn_link)
        self.radioBtn_random.Bind(wx.EVT_RADIOBUTTON, self.rdn_random)

        self.data_file_picker.Bind(wx.EVT_FILEPICKER_CHANGED, self.data_pick)
        self.data_test_file.Bind(wx.EVT_FILEPICKER_CHANGED, self.data_test_pick)

        self.run_algo.Bind(wx.EVT_BUTTON, self.start_btn)
        self.Bind(wx.EVT_MENU, self.classification_Support_vector_machines,
                  id=self.menu_classification_Support_vector_machines.GetId())
        self.Bind(wx.EVT_MENU, self.classification_Stochastic_gradient_descent,
                  id=self.menu_classification_Stochastic_gradient_descent.GetId())
        self.Bind(wx.EVT_MENU, self.classification_Nearest_Neighbors,
                  id=self.menu_classification_Nearest_Neighbors.GetId())
        self.Bind(wx.EVT_MENU, self.classification_Gaussian_Processes,
                  id=self.menu_classification_Gaussian_Processes.GetId())
        self.Bind(wx.EVT_MENU, self.classification_Decision_trees, id=self.menu_classification_Decision_trees.GetId())
        self.Bind(wx.EVT_MENU, self.classification_naiv_bais, id=self.menu_classification_naiv_bais.GetId())
        self.Bind(wx.EVT_MENU, self.classification_kmeanes, id=self.menu_classification_kmeanes.GetId())
        self.Bind(wx.EVT_MENU, self.classification_less_sqad, id=self.menu_classification_less_sqad.GetId())
        self.Bind(wx.EVT_MENU, self.classification_rokkio, id=self.menu_classification_rokkio.GetId())
        self.Bind(wx.EVT_MENU, self.classification_vectors, id=self.menu_classification_vectors.GetId())
        self.Bind(wx.EVT_MENU, self.clusterization_kmeans, id=self.menu_clusterization_kmeans.GetId())
        self.Bind(wx.EVT_MENU, self.clusterization_id3, id=self.menu_clusterization_id3.GetId())
        self.Bind(wx.EVT_MENU, self.clusterization_Affinity_Propagation,
                  id=self.menu_clusterization_Affinity_Propagation.GetId())
        self.Bind(wx.EVT_MENU, self.clusterization_Birch, id=self.menu_clusterization_Birch.GetId())
        self.Bind(wx.EVT_MENU, self.clusterization_Mean_Shift, id=self.menu_clusterization_Mean_Shift.GetId())
        self.Bind(wx.EVT_MENU, self.clusterization_Perfomance_evalution,
                  id=self.menu_clusterization_Perfomance_evalution.GetId())
        self.Bind(wx.EVT_MENU, self.clusterization_Hierarchical_clustering,
                  id=self.menu_clusterization_Hierarchical_clustering.GetId())
        self.Bind(wx.EVT_MENU, self.clusterization_Adjusted_Rand_index,
                  id=self.menu_clusterization_Adjusted_Rand_index.GetId())
        self.Bind(wx.EVT_MENU, self.clusterization_DBSCAN, id=self.menu_clusterization_DBSCAN.GetId())
        self.Bind(wx.EVT_MENU, self.clusterization_MutualInformationbasedscore,
                  id=self.menu_clusterization_MutualInformationbasedscore.GetId())
        self.Bind(wx.EVT_MENU, self.clusterization_Silhouette_Coefficient,
                  id=self.menu_clusterization_Silhouette_Coefficient.GetId())
        self.Bind(wx.EVT_MENU, self.clusterization_Fowlkes_Mallows_scores,
                  id=self.menu_clusterization_Fowlkes_Mallows_scores.GetId())
        self.Bind(wx.EVT_MENU, self.clusterization_V_measure, id=self.menu_clusterization_V_measure.GetId())
        self.Bind(wx.EVT_MENU, self.clusterization_Spectral_clustering,
                  id=self.menu_clusterization_Spectral_clustering.GetId())
        self.Bind(wx.EVT_MENU, self.asociative_rules_apriori, id=self.menu_asociative_rules_apriori.GetId())
        self.Bind(wx.EVT_MENU, self.asociative_rules_aprioriTID, id=self.menu_asociative_rules_aprioriTID.GetId())
        self.Bind(wx.EVT_MENU, self.asociative_rules_aprioriHybrid, id=self.menu_asociative_rules_aprioriHybrid.GetId())
        self.Bind(wx.EVT_MENU, self.asociative_rules_DHP, id=self.menu_asociative_rules_DHP.GetId())
        self.Bind(wx.EVT_MENU, self.asociative_rules_PARTITION, id=self.menu_asociative_rules_PARTITION.GetId())

    def __del__(self):
        pass

    # region Выбор задачи
    def classification_Support_vector_machines(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: Support vector machines")
        self.algo_state.SetLabel('classification_Support_vector_machines')

    def classification_Stochastic_gradient_descent(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: Stochastic gradient descent")
        self.algo_state.SetLabel('classification_Stochastic_gradient_descent')

    def classification_Nearest_Neighbors(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: Nearest Neighbors")
        self.algo_state.SetLabel('classification_Nearest_Neighbors')

    def classification_Gaussian_Processes(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: Gaussian Processes")
        self.algo_state.SetLabel('classification_Gaussian_Processes')

    def classification_Decision_trees(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: Decision trees")
        self.algo_state.SetLabel('classification_Decision_trees')

    def classification_naiv_bais(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: Наивная байесовская классификация")
        self.algo_state.SetLabel('classification_naiv_bais')

    def classification_kmeanes(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: K ближайших соседей")
        self.algo_state.SetLabel('classification_kmeanes')

    def classification_less_sqad(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: Наименьших квадратов")
        self.algo_state.SetLabel('classification_less_sqad')

    def classification_rokkio(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: Rokkio")
        self.algo_state.SetLabel('classification_rokkio')

    def classification_vectors(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: Опорных векторов")
        self.algo_state.SetLabel('classification_vectors')

    def clusterization_kmeans(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: K-means")
        self.algo_state.SetLabel('clusterization_kmeans')

    def clusterization_id3(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: id3")
        self.algo_state.SetLabel('clusterization_id3')

    def clusterization_Affinity_Propagation(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Affinity Propagation")
        self.algo_state.SetLabel('clusterization_Affinity_Propagation')

    def clusterization_Birch(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Birch")
        self.algo_state.SetLabel('clusterization_Birch')

    def clusterization_Mean_Shift(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Mean Shift")
        self.algo_state.SetLabel('clusterization_Mean_Shift')

    def clusterization_Perfomance_evalution(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Perfomance evalution")
        self.algo_state.SetLabel('clusterization_Perfomance_evalution')

    def clusterization_Hierarchical_clustering(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Hierarchical clustering")
        self.algo_state.SetLabel('clusterization_Hierarchical_clustering')

    def clusterization_Adjusted_Rand_index(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Adjusted Rand index")
        self.algo_state.SetLabel('clusterization_Adjusted_Rand_index')

    def clusterization_DBSCAN(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: DBSCAN")
        self.algo_state.SetLabel('clusterization_DBSCAN')

    def clusterization_MutualInformationbasedscore(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Mutual Information based score")
        self.algo_state.SetLabel('clusterization_MutualInformationbasedscore')

    def clusterization_Silhouette_Coefficient(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Silhouette Coefficient")
        self.algo_state.SetLabel('clusterization_Silhouette_Coefficient')

    def clusterization_Fowlkes_Mallows_scores(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Fowlkes Mallows scores")
        self.algo_state.SetLabel('clusterization_Fowlkes_Mallows_scores')

    def clusterization_V_measure(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: V-measure")
        self.algo_state.SetLabel('clusterization_V_measure')

    def clusterization_Spectral_clustering(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Spectral clustering")
        self.algo_state.SetLabel('clusterization_Spectral_clustering')

    def asociative_rules_apriori(self, event):
        self.lable_task.SetLabel("Задача: Поиск ассоциативных правил")
        self.lable_algo.SetLabel("Алгоритм: apriori")
        self.algo_state.SetLabel('asociative_rules_apriori')

    def asociative_rules_aprioriTID(self, event):
        self.lable_task.SetLabel("Задача: Поиск ассоциативных правил")
        self.lable_algo.SetLabel("Алгоритм: aprioriTID")
        self.algo_state.SetLabel('asociative_rules_aprioriTID')

    def asociative_rules_aprioriHybrid(self, event):
        self.lable_task.SetLabel("Задача: Поиск ассоциативных правил")
        self.lable_algo.SetLabel("Алгоритм: aprioriHybrid")
        self.algo_state.SetLabel('asociative_rules_aprioriHybrid')

    def asociative_rules_DHP(self, event):
        self.lable_task.SetLabel("Задача: Поиск ассоциативных правил")
        self.lable_algo.SetLabel("Алгоритм: DHP")
        self.algo_state.SetLabel('asociative_rules_DHP')

    def asociative_rules_PARTITION(self, event):
        self.lable_task.SetLabel("Задача: Поиск ассоциативных правил")
        self.lable_algo.SetLabel("Алгоритм: PARTITION")
        self.algo_state.SetLabel('asociative_rules_PARTITION')

    # endregion

    # Общие

    def rdn_file(self, event):
        self.data_file_picker.Enable(True)
        self.data_link.Enable(False)

    def data_pick(self, event):
        event.Skip()

    def rdn_link(self, event):
        self.data_file_picker.Enable(False)
        self.data_link.Enable(True)

    def rdn_random(self, event):
        self.data_file_picker.Enable(False)
        self.data_link.Enable(False)

    def data_test_pick(self, event):
        event.Skip()





    def file_path_local(self):
        path_to_file = os.path.abspath(self.data_file_picker.GetPath())
        return path_to_file

    def file_path_web(self):
        path_to_file = self.data_link.GetValue()
        return path_to_file



    def file_type_check(self):
        current_file = 'empty'
        if self.file_path_local().endswith('.csv'):
            current_file = 'csv'
        elif self.file_path_local().endswith('.txt'):
            current_file = 'txt'
        return current_file

    def file_type_check_web(self):
        current_file = 'empty'
        if self.file_path_web().endswith('.csv'):
            current_file = 'csv'
        elif self.file_path_web().endswith('.txt'):
            current_file = 'txt'
        return current_file


    def data_from_internet_csv(self):
        data_temp = io.Input.internet_read_csv(self.file_path_web)
        print('test')
        return data_temp

    def data_from_internet_txt(self):
        data_temp = io.Input.internet_read_text_file(self.file_path_web)
        print('test')
        return data_temp

    def data_from_local_csv(self):
        data_temp = io.Input.local_read_csv(self.file_path_local())
        print('test')
        return data_temp

    def data_from_local_txt(self):
        data_temp = io.Input.local_read_text_file(self.file_path_local())
        print('test')
        return data_temp



    def start_btn(self, event):
        if self.lable_algo.GetLabel() != 'Алгоритм: Не выбран':
            # Работа с локальным файлом
            if self.radioBtn_data_file.GetValue():
                if self.file_type_check() != 'empty':
                    if self.algo_state.GetLabel() == 'classification_Support_vector_machines':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")


                    elif self.algo_state.GetLabel() == 'classification_Stochastic_gradient_descent':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'classification_Nearest_Neighbors':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'classification_Gaussian_Processes':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")


                    elif self.algo_state.GetLabel() == 'classification_Decision_trees':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'classification_naiv_bais':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'classification_kmeanes':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'classification_less_sqad':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'classification_rokkio':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'classification_vectors':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_kmeans':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            k_means.run_kmeans(self.file_path_local())

                    elif self.algo_state.GetLabel() == 'clusterization_id3':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Affinity_Propagation':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Birch':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Mean_Shift':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Perfomance_evalution':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Hierarchical_clustering':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Adjusted_Rand_index':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_DBSCAN':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_MutualInformationbasedscore':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Silhouette_Coefficient':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Fowlkes_Mallows_scores':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_V_measure':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Spectral_clustering':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'asociative_rules_apriori':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'asociative_rules_aprioriTID':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'asociative_rules_aprioriHybrid':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'asociative_rules_DHP':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'asociative_rules_PARTITION':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                else:
                    wx.MessageBox("Файл не указан или имеет неверный формат")

            # Работа с веб файлом
            elif self.radioBtn_link.GetValue():
                if self.file_type_check_web() != 'empty':
                    if self.algo_state.GetLabel() == 'classification_Support_vector_machines':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")


                    elif self.algo_state.GetLabel() == 'classification_Stochastic_gradient_descent':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'classification_Nearest_Neighbors':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'classification_Gaussian_Processes':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")


                    elif self.algo_state.GetLabel() == 'classification_Decision_trees':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'classification_naiv_bais':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'classification_kmeanes':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'classification_less_sqad':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'classification_rokkio':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'classification_vectors':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_kmeans':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            k_means.run_kmeans(self.file_path_local())

                    elif self.algo_state.GetLabel() == 'clusterization_id3':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Affinity_Propagation':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Birch':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Mean_Shift':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Perfomance_evalution':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Hierarchical_clustering':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Adjusted_Rand_index':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_DBSCAN':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_MutualInformationbasedscore':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Silhouette_Coefficient':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Fowlkes_Mallows_scores':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_V_measure':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'clusterization_Spectral_clustering':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'asociative_rules_apriori':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'asociative_rules_aprioriTID':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'asociative_rules_aprioriHybrid':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'asociative_rules_DHP':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                    elif self.algo_state.GetLabel() == 'asociative_rules_PARTITION':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("OMG! THIS IS PROBLEM!")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("OMG! THIS IS PROBLEM v2!")

                else:
                    wx.MessageBox("URL не указан или имеет неверный формат")

            elif self.radioBtn_random.GetValue():
                wx.MessageBox("Рандома не будет")
        else:
            wx.MessageBox("Выберите алгоритм")


app = wx.App(False)
frame = MainWindow(None)
frame.Show()
app.MainLoop()
