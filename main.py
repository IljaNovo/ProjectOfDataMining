# -*- coding: utf-8 -*- 


import wx
import wx.xrc

import input_output.io as io
import os.path

import classification.C_4_5.tree as c45
import classification.Naive_Bayes_Classifier.BayesScratch.bayes_classifier as bayes
import classification.k_Nearest_Neighbors.knn as knn
import classification.Stochastic_Gradient_Descent.sgd as sgd
import classification.Support_Vector_Machine.support_vector_machine as svm
import classification.Linear_Least_Squares_Classifier.LLS as lls
import classification.Decision_Tree_Classification.decision_tree_classification as dtc

import clustering.Hierarchical_clustering.hclust as hc
import clustering.Hierarchical_clustering.hierarchical_clustering_plot as hc_plot
import clustering.DBSCAN.plot_dbscan as dbscan
import clustering.BIRCH.birch_clustering as birch
import clustering.mean_shift.mean_shift as mean_shift
import clustering.k_means.k_means_plt as k_means_csv
import clustering.k_means.k_means as k_means
import clustering.Affinity_Propagation.AffinityPropagation as aff_p

from associative_rules.apriori_tid.apriori import *


###########################################################################
## Class MainWindow
###########################################################################




class MainWindow(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Data Mining", pos=wx.DefaultPosition,
                          size=wx.Size(320, 530), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetSizeHints(wx.Size(320, 530), wx.Size(470, 530))

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
        self.menu_classification_naive_bayes = wx.MenuItem(self.menu_classification, wx.ID_ANY,
                                                         u"Наивная Байесовская классификация", wx.EmptyString,
                                                         wx.ITEM_NORMAL)
        self.menu_classification.Append(self.menu_classification_naive_bayes)

        self.menu_classification_less_sqad = wx.MenuItem(self.menu_classification, wx.ID_ANY,
                                                         u"Алгоритм наименьших квадратов", wx.EmptyString,
                                                         wx.ITEM_NORMAL)
        self.menu_classification.Append(self.menu_classification_less_sqad)
        self.menu.AppendSubMenu(self.menu_classification, u"Классификация")
        # endregion

        # region Меню/Кластеризация
        self.menu_clustering = wx.Menu()

        self.menu_clustering_kmeans = wx.MenuItem(self.menu_clustering, wx.ID_ANY, u"K-means", wx.EmptyString,
                                                      wx.ITEM_NORMAL)
        self.menu_clustering.Append(self.menu_clustering_kmeans)
        self.menu_clustering_id3 = wx.MenuItem(self.menu_clustering, wx.ID_ANY, u"ID3", wx.EmptyString,
                                                   wx.ITEM_NORMAL)
        self.menu_clustering.Append(self.menu_clustering_id3)
        self.menu_clustering_Affinity_Propagation = wx.MenuItem(self.menu_clustering, wx.ID_ANY,
                                                                    u"Affinity Propagation", wx.EmptyString,
                                                                    wx.ITEM_NORMAL)
        self.menu_clustering.Append(self.menu_clustering_Affinity_Propagation)
        self.menu_clustering_Birch = wx.MenuItem(self.menu_clustering, wx.ID_ANY, u"Birch", wx.EmptyString,
                                                     wx.ITEM_NORMAL)
        self.menu_clustering.Append(self.menu_clustering_Birch)
        self.menu_clustering_Mean_Shift = wx.MenuItem(self.menu_clustering, wx.ID_ANY, u"Mean Shift",
                                                          wx.EmptyString,
                                                          wx.ITEM_NORMAL)
        self.menu_clustering.Append(self.menu_clustering_Mean_Shift)
        self.menu_clustering_Perfomance_evalution = wx.MenuItem(self.menu_clustering, wx.ID_ANY,
                                                                    u"Perfomance evalution", wx.EmptyString,
                                                                    wx.ITEM_NORMAL)
        self.menu_clustering.Append(self.menu_clustering_Perfomance_evalution)
        self.menu_clustering_Hierarchical_clustering = wx.MenuItem(self.menu_clustering, wx.ID_ANY,
                                                                       u"Hierarchical clustering", wx.EmptyString,
                                                                       wx.ITEM_NORMAL)
        self.menu_clustering.Append(self.menu_clustering_Hierarchical_clustering)
        self.menu_clustering_Adjusted_Rand_index = wx.MenuItem(self.menu_clustering, wx.ID_ANY,
                                                                   u"Adjusted Rand index", wx.EmptyString,
                                                                   wx.ITEM_NORMAL)
        self.menu_clustering.Append(self.menu_clustering_Adjusted_Rand_index)
        self.menu_clustering_DBSCAN = wx.MenuItem(self.menu_clustering, wx.ID_ANY, u"DBSCAN", wx.EmptyString,
                                                      wx.ITEM_NORMAL)
        self.menu_clustering.Append(self.menu_clustering_DBSCAN)
        self.menu_clustering_MutualInformationbasedscore = wx.MenuItem(self.menu_clustering, wx.ID_ANY,
                                                                           u"Mutual Information based score",
                                                                           wx.EmptyString,
                                                                           wx.ITEM_NORMAL)
        self.menu_clustering.Append(self.menu_clustering_MutualInformationbasedscore)
        self.menu_clustering_Silhouette_Coefficient = wx.MenuItem(self.menu_clustering, wx.ID_ANY,
                                                                      u"Silhouette Coefficient", wx.EmptyString,
                                                                      wx.ITEM_NORMAL)
        self.menu_clustering.Append(self.menu_clustering_Silhouette_Coefficient)
        self.menu_clustering_V_measure = wx.MenuItem(self.menu_clustering, wx.ID_ANY, u"V-measure",
                                                         wx.EmptyString,
                                                         wx.ITEM_NORMAL)
        self.menu_clustering.Append(self.menu_clustering_V_measure)
        self.menu_clustering_Spectral_clustering = wx.MenuItem(self.menu_clustering, wx.ID_ANY,
                                                                   u"Spectral clustering", wx.EmptyString,
                                                                   wx.ITEM_NORMAL)
        self.menu_clustering.Append(self.menu_clustering_Spectral_clustering)
        self.menu.AppendSubMenu(self.menu_clustering, u"Кластеризация")
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


        #Выклчюенные элементы меню
        self.menu_classification_Gaussian_Processes.Enable(False)
        self.menu_classification_less_sqad.Enable(False)
        self.menu_clustering_id3.Enable(False)
        self.menu_clustering_Perfomance_evalution.Enable(False)
        self.menu_clustering_Adjusted_Rand_index.Enable(False)
        self.menu_clustering_MutualInformationbasedscore.Enable(False)
        self.menu_clustering_Silhouette_Coefficient.Enable(False)
        self.menu_clustering_V_measure.Enable(False)
        self.menu_clustering_Spectral_clustering.Enable(False)
        self.menu_asociative_rules_apriori.Enable(False)
        self.menu_asociative_rules_aprioriHybrid.Enable(False)
        self.menu_asociative_rules_DHP.Enable(False)
        self.menu_asociative_rules_PARTITION.Enable(False)
        # endregion



        # region Интерфейс
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

        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 270,-1 ), wx.LI_HORIZONTAL)
        gbSizer1.Add(self.m_staticline1, wx.GBPosition(2, 1), wx.GBSpan(1, 8), wx.EXPAND | wx.ALL, 9)

        self.lable_choice_data = wx.StaticText(self, wx.ID_ANY, u"Использовать данные из:", wx.DefaultPosition,
                                               wx.Size(-1, -1), wx.ALIGN_CENTRE)
        self.lable_choice_data.Wrap(-1)
        self.lable_choice_data.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))
        self.lable_choice_data.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_APPWORKSPACE))

        gbSizer1.Add(self.lable_choice_data, wx.GBPosition(3, 1), wx.GBSpan(1, 8), wx.ALL | wx.EXPAND, 5)

        self.radioBtn_data_file = wx.RadioButton(self, wx.ID_ANY, u"Файла", wx.DefaultPosition, wx.DefaultSize, 0)
        self.radioBtn_data_file.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL,
                    False, wx.EmptyString))

        gbSizer1.Add(self.radioBtn_data_file, wx.GBPosition(4, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.data_file_picker = wx.FilePickerCtrl(self, wx.ID_ANY, u"Укажите путь к файлу", u"Выберите файл",
                                                  u"data (*.csv,*.txt)|*.csv;*.txt", wx.DefaultPosition,
                                                  wx.DefaultSize, wx.FLP_DEFAULT_STYLE | wx.FLP_SMALL)
        gbSizer1.Add(self.data_file_picker, wx.GBPosition(5, 1), wx.GBSpan(1, 8), wx.ALL | wx.EXPAND, 5)
        self.data_file_picker.Enable(False)

        self.radioBtn_link = wx.RadioButton(self, wx.ID_ANY, u"Интернета (URL)", wx.DefaultPosition, wx.DefaultSize, 0)
        self.radioBtn_link.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL,
                    False, wx.EmptyString))

        gbSizer1.Add(self.radioBtn_link, wx.GBPosition(6, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.data_link = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                     wx.TE_AUTO_URL)
        gbSizer1.Add(self.data_link, wx.GBPosition(7, 1), wx.GBSpan(1, 8), wx.ALL | wx.EXPAND, 5)
        self.data_link.Enable(False)

        self.radioBtn_random = wx.RadioButton(self, wx.ID_ANY, u"Случайные", wx.DefaultPosition, wx.DefaultSize, 0)
        self.radioBtn_random.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL,
                    False, wx.EmptyString))

        gbSizer1.Add(self.radioBtn_random, wx.GBPosition(8, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.m_staticline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        gbSizer1.Add(self.m_staticline2, wx.GBPosition(9, 1), wx.GBSpan(1, 8), wx.EXPAND | wx.ALL, 9)

        self.lable_settings = wx.StaticText(self, wx.ID_ANY, u"Настройки", wx.DefaultPosition, wx.DefaultSize,
                                           wx.ALIGN_CENTRE)
        self.lable_settings.Wrap(-1)
        self.lable_settings.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        gbSizer1.Add(self.lable_settings, wx.GBPosition(10, 1), wx.GBSpan(1, 8), wx.ALL | wx.EXPAND, 5)

        self.settings_lable_1 = wx.StaticText(self, wx.ID_ANY, u"Параметр#1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.settings_lable_1.Wrap(-1)
        self.settings_lable_1.Enable(False)
        gbSizer1.Add(self.settings_lable_1, wx.GBPosition(11, 1), wx.GBSpan(1, 2), wx.ALL, 8)

        self.settings_value_1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.settings_value_1.Enable(False)
        gbSizer1.Add(self.settings_value_1, wx.GBPosition(11, 3), wx.GBSpan(1, 5), wx.ALL|wx.EXPAND, 5)

        self.settings_lable_2 = wx.StaticText(self, wx.ID_ANY, u"Параметр#2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.settings_lable_2.Enable(False)
        self.settings_lable_2.Wrap(-1)
        gbSizer1.Add(self.settings_lable_2, wx.GBPosition(12, 1), wx.GBSpan(1, 2), wx.ALL, 8)

        self.settings_value_2 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.settings_value_2.Enable(False)
        gbSizer1.Add(self.settings_value_2, wx.GBPosition(12, 3), wx.GBSpan(1, 5), wx.ALL|wx.EXPAND, 5)

        self.settings_lable_3 = wx.StaticText(self, wx.ID_ANY, u"Параметр#3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.settings_lable_3.Enable(False)
        self.settings_lable_3.Wrap(-1)
        gbSizer1.Add(self.settings_lable_3, wx.GBPosition(13, 1), wx.GBSpan(1, 2), wx.ALL, 8)

        self.settings_value_3 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.settings_value_3.Enable(False)
        gbSizer1.Add(self.settings_value_3, wx.GBPosition(13, 3), wx.GBSpan(1, 5), wx.ALL|wx.EXPAND, 5)

        self.m_staticline3 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        gbSizer1.Add(self.m_staticline3, wx.GBPosition(14, 1), wx.GBSpan(1, 8), wx.EXPAND | wx.ALL, 9)

        self.run_algo = wx.Button(self, wx.ID_ANY, u"Выполнить", wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.run_algo, wx.GBPosition(15, 1), wx.GBSpan(4, 8), wx.ALL | wx.EXPAND, 5)

        self.algo_state = wx.StaticText(self, wx.ID_ANY, u"empty", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.algo_state.Wrap(-1)
        self.algo_state.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD,
                    False, wx.EmptyString))

        gbSizer1.Add(self.algo_state, wx.GBPosition(30, 1), wx.GBSpan(1, 20), wx.ALL, 5)

        self.SetSizer(gbSizer1)
        self.Layout()

        self.Centre(wx.BOTH)
        # endregion



        # region События
        self.radioBtn_data_file.Bind(wx.EVT_RADIOBUTTON, self.rdn_file)
        self.radioBtn_link.Bind(wx.EVT_RADIOBUTTON, self.rdn_link)
        self.radioBtn_random.Bind(wx.EVT_RADIOBUTTON, self.rdn_random)

        self.data_file_picker.Bind(wx.EVT_FILEPICKER_CHANGED, self.data_pick)

        self.run_algo.Bind(wx.EVT_BUTTON, self.start_btn)

        self.settings_value_1.Bind(wx.EVT_CHAR, self.check_input)
        self.settings_value_2.Bind(wx.EVT_CHAR, self.check_input)
        self.settings_value_3.Bind(wx.EVT_CHAR, self.check_input)

        self.Bind(wx.EVT_MENU, self.classification_Support_vector_machines,
                  id=self.menu_classification_Support_vector_machines.GetId())
        self.Bind(wx.EVT_MENU, self.classification_Stochastic_gradient_descent,
                  id=self.menu_classification_Stochastic_gradient_descent.GetId())
        self.Bind(wx.EVT_MENU, self.classification_Nearest_Neighbors,
                  id=self.menu_classification_Nearest_Neighbors.GetId())
        self.Bind(wx.EVT_MENU, self.classification_Gaussian_Processes,
                  id=self.menu_classification_Gaussian_Processes.GetId())
        self.Bind(wx.EVT_MENU, self.classification_Decision_trees, id=self.menu_classification_Decision_trees.GetId())
        self.Bind(wx.EVT_MENU, self.classification_naive_bayes, id=self.menu_classification_naive_bayes.GetId())
        self.Bind(wx.EVT_MENU, self.classification_less_sqad, id=self.menu_classification_less_sqad.GetId())
        self.Bind(wx.EVT_MENU, self.clustering_kmeans, id=self.menu_clustering_kmeans.GetId())
        self.Bind(wx.EVT_MENU, self.clustering_id3, id=self.menu_clustering_id3.GetId())
        self.Bind(wx.EVT_MENU, self.clustering_Affinity_Propagation,
                  id=self.menu_clustering_Affinity_Propagation.GetId())
        self.Bind(wx.EVT_MENU, self.clustering_Birch, id=self.menu_clustering_Birch.GetId())
        self.Bind(wx.EVT_MENU, self.clustering_Mean_Shift, id=self.menu_clustering_Mean_Shift.GetId())
        self.Bind(wx.EVT_MENU, self.clustering_Perfomance_evalution,
                  id=self.menu_clustering_Perfomance_evalution.GetId())
        self.Bind(wx.EVT_MENU, self.clustering_Hierarchical_clustering,
                  id=self.menu_clustering_Hierarchical_clustering.GetId())
        self.Bind(wx.EVT_MENU, self.clustering_Adjusted_Rand_index,
                  id=self.menu_clustering_Adjusted_Rand_index.GetId())
        self.Bind(wx.EVT_MENU, self.clustering_DBSCAN, id=self.menu_clustering_DBSCAN.GetId())
        self.Bind(wx.EVT_MENU, self.clustering_MutualInformationbasedscore,
                  id=self.menu_clustering_MutualInformationbasedscore.GetId())
        self.Bind(wx.EVT_MENU, self.clustering_Silhouette_Coefficient,
                  id=self.menu_clustering_Silhouette_Coefficient.GetId())
        self.Bind(wx.EVT_MENU, self.clustering_V_measure, id=self.menu_clustering_V_measure.GetId())
        self.Bind(wx.EVT_MENU, self.clustering_Spectral_clustering,
                  id=self.menu_clustering_Spectral_clustering.GetId())
        self.Bind(wx.EVT_MENU, self.asociative_rules_apriori, id=self.menu_asociative_rules_apriori.GetId())
        self.Bind(wx.EVT_MENU, self.asociative_rules_aprioriTID, id=self.menu_asociative_rules_aprioriTID.GetId())
        self.Bind(wx.EVT_MENU, self.asociative_rules_aprioriHybrid, id=self.menu_asociative_rules_aprioriHybrid.GetId())
        self.Bind(wx.EVT_MENU, self.asociative_rules_DHP, id=self.menu_asociative_rules_DHP.GetId())
        self.Bind(wx.EVT_MENU, self.asociative_rules_PARTITION, id=self.menu_asociative_rules_PARTITION.GetId())
        #endregion


    def __del__(self):
        pass

    # region Выбор задачи
    def advanced_settings_disable(self): # Сброс и отключение элемнетов расширенной настройки
        self.settings_lable_1.Enable(False)
        self.settings_lable_2.Enable(False)
        self.settings_lable_3.Enable(False)

        self.settings_lable_1.SetLabel('Параметр#1')
        self.settings_lable_2.SetLabel('Параметр#2')
        self.settings_lable_3.SetLabel('Параметр#3')

        self.settings_value_1.Enable(False)
        self.settings_value_2.Enable(False)
        self.settings_value_3.Enable(False)

        self.settings_value_1.SetValue('')
        self.settings_value_2.SetValue('')
        self.settings_value_3.SetValue('')



    def classification_Support_vector_machines(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: Support vector machines")
        self.algo_state.SetLabel('classification_Support_vector_machines')
        self.advanced_settings_disable()

    def classification_Stochastic_gradient_descent(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: Stochastic gradient descent")
        self.algo_state.SetLabel('classification_Stochastic_gradient_descent')
        self.advanced_settings_disable()
        self.settings_lable_1.Enable(True)
        self.settings_lable_1.SetLabel('Размер шага в сетке')
        self.settings_value_1.Enable(True)
        self.settings_value_1.SetValue('0.02')

    def classification_Nearest_Neighbors(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: Nearest Neighbors")
        self.algo_state.SetLabel('classification_Nearest_Neighbors')
        self.advanced_settings_disable()
        self.settings_lable_1.Enable(True)
        self.settings_lable_1.SetLabel('n_neighbors')
        self.settings_value_1.Enable(True)
        self.settings_value_1.SetValue('15')
        self.settings_lable_2.Enable(True)
        self.settings_lable_2.SetLabel('Размер шага в сетке')
        self.settings_value_2.Enable(True)
        self.settings_value_2.SetValue('0.02')

    def classification_Gaussian_Processes(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: Gaussian Processes")
        self.algo_state.SetLabel('classification_Gaussian_Processes')
        self.advanced_settings_disable()

    def classification_Decision_trees(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: Decision trees")
        self.algo_state.SetLabel('classification_Decision_trees')
        self.advanced_settings_disable()
        self.settings_value_1.Enable(True)
        self.settings_lable_1.Enable(True)
        self.settings_lable_1.SetLabel('Кол-во проходов')
        self.settings_value_1.SetValue('6')

    def classification_naive_bayes(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: Наивная байесовская классификация")
        self.algo_state.SetLabel('classification_naive_bayes')
        self.advanced_settings_disable()
        self.settings_value_1.Enable(True)
        self.settings_lable_1.Enable(True)
        self.settings_lable_1.SetLabel('SplitRatio')
        self.settings_value_1.SetValue('0.67')

    def classification_less_sqad(self, event):
        self.lable_task.SetLabel("Задача: Классификация")
        self.lable_algo.SetLabel("Алгоритм: Наименьших квадратов")
        self.algo_state.SetLabel('classification_less_sqad')
        self.advanced_settings_disable()

    def clustering_kmeans(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: K-means")
        self.algo_state.SetLabel('clustering_kmeans')
        self.advanced_settings_disable()
        self.settings_lable_1.Enable(True)
        self.settings_lable_1.SetLabel('Размерность')
        self.settings_value_1.Enable(True)
        self.settings_value_1.SetValue('3')

    def clustering_id3(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: id3")
        self.algo_state.SetLabel('clustering_id3')
        self.advanced_settings_disable()

    def clustering_Affinity_Propagation(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Affinity Propagation")
        self.algo_state.SetLabel('clustering_Affinity_Propagation')
        self.advanced_settings_disable()
        self.settings_lable_1.Enable(True)
        self.settings_lable_1.SetLabel('Предпочтение')
        self.settings_value_1.Enable(True)
        self.settings_value_1.SetValue('-50')

    def clustering_Birch(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Birch")
        self.algo_state.SetLabel('clustering_Birch')
        self.advanced_settings_disable()
        self.settings_lable_1.Enable(True)
        self.settings_lable_1.SetLabel('Радиус кластера')
        self.settings_value_1.Enable(True)
        self.settings_value_1.SetValue('1.7')
        self.settings_lable_2.Enable(True)
        self.settings_lable_2.SetLabel('Кол-во кластеров')
        self.settings_value_2.Enable(True)
        self.settings_value_2.SetValue('100')

    def clustering_Mean_Shift(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Mean Shift")
        self.algo_state.SetLabel('clustering_Mean_Shift')
        self.advanced_settings_disable()
        self.settings_lable_1.Enable(True)
        self.settings_lable_1.SetLabel('Пропускная способность')
        self.settings_value_1.Enable(True)
        self.settings_value_1.SetValue('1.04388')

    def clustering_Perfomance_evalution(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Perfomance evalution")
        self.algo_state.SetLabel('clustering_Perfomance_evalution')
        self.advanced_settings_disable()

    def clustering_Hierarchical_clustering(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Hierarchical clustering")
        self.algo_state.SetLabel('clustering_Hierarchical_clustering')
        self.advanced_settings_disable()
        self.settings_lable_1.Enable(True)
        self.settings_lable_1.SetLabel('Кол-во кластеров')
        self.settings_value_1.Enable(True)
        self.settings_value_1.SetValue('6')

    def clustering_Adjusted_Rand_index(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Adjusted Rand index")
        self.algo_state.SetLabel('clustering_Adjusted_Rand_index')
        self.advanced_settings_disable()

    def clustering_DBSCAN(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: DBSCAN")
        self.algo_state.SetLabel('clustering_DBSCAN')
        self.advanced_settings_disable()
        self.settings_lable_1.Enable(True)
        self.settings_lable_1.SetLabel('Eps')
        self.settings_value_1.Enable(True)
        self.settings_value_1.SetValue('0.3')
        self.settings_lable_2.Enable(True)
        self.settings_lable_2.SetLabel('Мин. кол-во сэмплов')
        self.settings_value_2.Enable(True)
        self.settings_value_2.SetValue('10')

    def clustering_MutualInformationbasedscore(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Mutual Information based score")
        self.algo_state.SetLabel('clustering_MutualInformationbasedscore')
        self.advanced_settings_disable()

    def clustering_Silhouette_Coefficient(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Silhouette Coefficient")
        self.algo_state.SetLabel('clustering_Silhouette_Coefficient')
        self.advanced_settings_disable()

    def clustering_V_measure(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: V-measure")
        self.algo_state.SetLabel('clustering_V_measure')
        self.advanced_settings_disable()

    def clustering_Spectral_clustering(self, event):
        self.lable_task.SetLabel("Задача: Кластеризация")
        self.lable_algo.SetLabel("Алгоритм: Spectral clustering")
        self.algo_state.SetLabel('clustering_Spectral_clustering')
        self.advanced_settings_disable()

    def asociative_rules_apriori(self, event):
        self.lable_task.SetLabel("Задача: Поиск ассоциативных правил")
        self.lable_algo.SetLabel("Алгоритм: apriori")
        self.algo_state.SetLabel('asociative_rules_apriori')
        self.advanced_settings_disable()

    def asociative_rules_aprioriTID(self, event):
        self.lable_task.SetLabel("Задача: Поиск ассоциативных правил")
        self.lable_algo.SetLabel("Алгоритм: aprioriTID")
        self.algo_state.SetLabel('asociative_rules_aprioriTID')
        self.advanced_settings_disable()
        self.settings_lable_1.Enable(True)
        self.settings_lable_1.SetLabel('min. Support')
        self.settings_value_1.Enable(True)
        self.settings_value_1.SetValue('0.5')
        self.settings_lable_2.Enable(True)
        self.settings_lable_2.SetLabel('min. Confidence')
        self.settings_value_2.Enable(True)
        self.settings_value_2.SetValue('0.05')

    def asociative_rules_aprioriHybrid(self, event):
        self.lable_task.SetLabel("Задача: Поиск ассоциативных правил")
        self.lable_algo.SetLabel("Алгоритм: aprioriHybrid")
        self.algo_state.SetLabel('asociative_rules_aprioriHybrid')
        self.advanced_settings_disable()

    def asociative_rules_DHP(self, event):
        self.lable_task.SetLabel("Задача: Поиск ассоциативных правил")
        self.lable_algo.SetLabel("Алгоритм: DHP")
        self.algo_state.SetLabel('asociative_rules_DHP')
        self.advanced_settings_disable()

    def asociative_rules_PARTITION(self, event):
        self.lable_task.SetLabel("Задача: Поиск ассоциативных правил")
        self.lable_algo.SetLabel("Алгоритм: PARTITION")
        self.algo_state.SetLabel('asociative_rules_PARTITION')
        self.advanced_settings_disable()

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



    def file_path_local(self): #Получение полного локального пути к файлу
        path_to_file = os.path.abspath(self.data_file_picker.GetPath())
        return path_to_file

    def file_path_web(self): #Получение веб пути к файлу
        path_to_file = self.data_link.GetValue()
        return path_to_file



    def file_type_check(self): #Проверка расширения локального файла
        current_file = 'empty'
        if self.file_path_local().endswith('.csv'):
            current_file = 'csv'
        elif self.file_path_local().endswith('.txt'):
            current_file = 'txt'
        return current_file

    def file_type_check_web(self): #Проверка расширения веб файла
        current_file = 'empty'
        if self.file_path_web().endswith('.csv'):
            current_file = 'csv'
        elif self.file_path_web().endswith('.txt'):
            current_file = 'txt'
        return current_file



    def advanced_settings_int(self, var): #Конвертирование параметра в int
        a = int(float(var))
        return a

    def advanced_settings_float(self, var): #Конвертирование параметра в float
        a = float(var)
        return a

    def check_input(self, event): #Ограничение допустимых символов ввода
        key = event.GetKeyCode()
        acceptable_characters = "1234567890.-\b"
        if chr(key) in acceptable_characters:
            event.Skip()
            return
        else:
            return False



    def start_btn(self, event):
        if self.lable_algo.GetLabel() != 'Алгоритм: Не выбран':
            # Работа с локальным файлом
            if self.radioBtn_data_file.GetValue():
                if self.file_type_check() != 'empty':
                    ##### Классификация local
                    if self.algo_state.GetLabel() == 'classification_Support_vector_machines':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            data = io.Input.load_csv_for_classification(self.file_path_local())
                            svm.svm_run(data)

                    elif self.algo_state.GetLabel() == 'classification_Stochastic_gradient_descent':
                        h = self.advanced_settings_float(self.settings_value_1.GetValue())  # step size in the mesh
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            data = io.Input.load_csv_for_classification(self.file_path_local())
                            sgd.run(data, h)

                    elif self.algo_state.GetLabel() == 'classification_Nearest_Neighbors':
                        n_neighbors = self.advanced_settings_int(self.settings_value_1.GetValue())
                        h = self.advanced_settings_float(self.settings_value_2.GetValue())  # step size in the mesh
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            data = io.Input.load_csv_for_classification(self.file_path_local())
                            knn.run(data,n_neighbors,h)

                    elif self.algo_state.GetLabel() == 'classification_Gaussian_Processes':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                    elif self.algo_state.GetLabel() == 'classification_Decision_trees':
                        k = self.advanced_settings_int(self.settings_value_1.GetValue())
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            #parameters
                            n_classes = 3
                            plot_colors = "ryb"
                            plot_step = 0.02
                            data = io.Input.load_csv_for_classification(self.file_path_local())
                            dtc.dtc_run(data, n_classes,plot_colors,plot_step)
                    elif self.algo_state.GetLabel() == 'classification_naive_bayes':
                        splitRatio = self.advanced_settings_float(self.settings_value_1.GetValue())
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            bayes.main(self.file_path_local(), splitRatio)
                            wx.MessageBox("Naive Bayes result in !Results/classification_NBC_result.txt")
                            os_command_string = "notepad.exe !Results/classification_NBC_result.txt"
                            os.system(os_command_string)

                    elif self.algo_state.GetLabel() == 'classification_less_sqad':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")



                    ##### Кластеризация local
                    elif self.algo_state.GetLabel() == 'clustering_kmeans':
                        n_clusters = self.advanced_settings_int(self.settings_value_1.GetValue())
                        if self.file_type_check() == 'txt':
                            X = io.Input.get_ndarray_from_txt(self.file_path_local())
                            k_means.run_kmeans(X, n_clusters)
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                    elif self.algo_state.GetLabel() == 'clustering_id3':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                    elif self.algo_state.GetLabel() == 'clustering_Affinity_Propagation':
                        preference = self.advanced_settings_int(self.settings_value_1.GetValue())
                        if self.file_type_check() == 'txt':
                            X = io.Input.get_ndarray_from_txt(self.file_path_local())
                            aff_p.compute_affinity_propagation(preference, X)
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                    elif self.algo_state.GetLabel() == 'clustering_Birch':
                        threshold = self.advanced_settings_float(
                            self.settings_value_1.GetValue())  # maximum radius for cluster
                        clusters = self.advanced_settings_int(
                            self.settings_value_2.GetValue())  # count of clusters for BIRCH with global clustering
                        if self.file_type_check() == 'txt':
                             X = io.Input.get_ndarray_from_txt(self.file_path_local())
                             birch.run(X, threshold, clusters)
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                    elif self.algo_state.GetLabel() == 'clustering_Mean_Shift':
                        bandwidth = self.advanced_settings_float(self.settings_value_1.GetValue())
                        if self.file_type_check() == 'txt':
                            X = io.Input.get_ndarray_from_txt(self.file_path_local())
                            mean_shift.run_mean_shift(X, bandwidth)
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                    elif self.algo_state.GetLabel() == 'clustering_Perfomance_evalution':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                    elif self.algo_state.GetLabel() == 'clustering_Hierarchical_clustering':
                        n_clusters = self.advanced_settings_int(self.settings_value_1.GetValue())
                        if self.file_type_check() == 'txt':
                            X = io.Input.get_ndarray_from_txt(self.file_path_local())
                            hc_plot.run(X, n_clusters)
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                    elif self.algo_state.GetLabel() == 'clustering_Adjusted_Rand_index':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                    elif self.algo_state.GetLabel() == 'clustering_DBSCAN':
                        eps = self.advanced_settings_float(
                            self.settings_value_1.GetValue())  # maximum distance between two samples or them to be considered as in the same neighborhood
                        min_samples = self.advanced_settings_int(
                            self.settings_value_2.GetValue())  # The number of samples (or total weight) in a neighborhood for a point to be considered as a core point. This includes the point itself.
                        if self.file_type_check() == 'txt':
                            X = io.Input.get_ndarray_from_txt(self.file_path_local())
                            dbscan.dbscan_run(X, eps, min_samples)
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                    elif self.algo_state.GetLabel() == 'clustering_MutualInformationbasedscore':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                    elif self.algo_state.GetLabel() == 'clustering_Silhouette_Coefficient':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                    elif self.algo_state.GetLabel() == 'clustering_V_measure':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                    elif self.algo_state.GetLabel() == 'clustering_Spectral_clustering':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")




                    ##### Ассоциативные правила local
                    elif self.algo_state.GetLabel() == 'asociative_rules_apriori':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                    elif self.algo_state.GetLabel() == 'asociative_rules_aprioriTID':
                        minSupport = self.advanced_settings_float(self.settings_value_1.GetValue())
                        minConfidence = self.advanced_settings_float(self.settings_value_2.GetValue())
                        if self.file_type_check() == 'txt':
                            data_iter = dataFromFile(self.file_path_local())
                            items, rules = runApriori(data_iter, minSupport, minConfidence)
                            printResults(items, rules)
                        elif self.file_type_check() == 'csv':
                            data_iter = dataFromFile(self.file_path_local())
                            items, rules = runApriori(data_iter, minSupport, minConfidence)
                            printResults(items, rules)

                    elif self.algo_state.GetLabel() == 'asociative_rules_aprioriHybrid':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                    elif self.algo_state.GetLabel() == 'asociative_rules_DHP':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                    elif self.algo_state.GetLabel() == 'asociative_rules_PARTITION':
                        if self.file_type_check() == 'txt':
                            wx.MessageBox("Txt файлы временно не поддерживаются")
                        elif self.file_type_check() == 'csv':
                            wx.MessageBox("Csv файлы временно не поддерживаются")

                else:
                    wx.MessageBox("Файл не указан или имеет неверный формат")

            # Работа с веб файлом
            elif self.radioBtn_link.GetValue():
                if self.file_type_check_web() != 'empty':
                    ##### Классификация web
                    if self.algo_state.GetLabel() == 'classification_Support_vector_machines':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'classification_Stochastic_gradient_descent':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'classification_Nearest_Neighbors':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'classification_Gaussian_Processes':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'classification_Decision_trees':
                        k = self.advanced_settings_int(self.settings_value_1.GetValue())
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            data = io.Input.internet_read_csv(self.file_path_web())
                            c45.run_decision_tree(data, k)
                            wx.MessageBox("Decision trees (c4.5) result in classification\\C_4_5\\result.txt")
                            os_command_string = "notepad.exe classification/C_4_5/result.txt"
                            os.system(os_command_string)

                    elif self.algo_state.GetLabel() == 'classification_naive_bayes':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'classification_less_sqad':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")





                    ##### Кластеризация web
                    elif self.algo_state.GetLabel() == 'clustering_kmeans':
                        n_clusters = self.advanced_settings_int(self.settings_value_1.GetValue())
                        if self.file_type_check_web() == 'txt':
                            X = io.Input.get_ndarray_from_web_txt(self.file_path_web())
                            k_means.run_kmeans(X, n_clusters)
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'clustering_id3':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'clustering_Affinity_Propagation':
                        preference = self.advanced_settings_int(self.settings_value_1.GetValue())
                        if self.file_type_check_web() == 'txt':
                            X = io.Input.get_ndarray_from_web_txt(self.file_path_web())
                            aff_p.compute_affinity_propagation(preference, X)
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'clustering_Birch':
                        threshold = self.advanced_settings_float(
                            self.settings_value_1.GetValue())  # maximum radius for cluster
                        clusters = self.advanced_settings_int(
                            self.settings_value_2.GetValue())  # count of clusters for BIRCH with global clustering

                        if self.file_type_check_web() == 'txt':
                            X = io.Input.get_ndarray_from_web_txt(self.file_path_web())
                            birch.run(X, threshold, clusters)
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'clustering_Mean_Shift':
                        bandwidth = self.advanced_settings_float(self.settings_value_1.GetValue())
                        if self.file_type_check_web() == 'txt':
                            X = io.Input.get_ndarray_from_web_txt(self.file_path_web())
                            mean_shift.run_mean_shift(X, bandwidth)
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'clustering_Perfomance_evalution':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'clustering_Hierarchical_clustering':
                        n_clusters = self.advanced_settings_int(self.settings_value_1.GetValue())
                        if self.file_type_check_web() == 'txt':
                            X = io.Input.get_ndarray_from_web_txt(self.file_path_web())
                            hc_plot.run(X, n_clusters)
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'clustering_Adjusted_Rand_index':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'clustering_DBSCAN':
                        eps = self.advanced_settings_float(
                            self.settings_value_1.GetValue())  # maximum distance between two samples or them to be considered as in the same neighborhood
                        min_samples = self.advanced_settings_int(
                            self.settings_value_2.GetValue())  # The number of samples (or total weight) in a neighborhood for a point to be considered as a core point. This includes the point itself.
                        if self.file_type_check_web() == 'txt':
                            X = io.Input.get_ndarray_from_web_txt(self.file_path_web())
                            dbscan.dbscan_run(X, eps, min_samples)
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'clustering_MutualInformationbasedscore':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'clustering_Silhouette_Coefficient':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'clustering_V_measure':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'clustering_Spectral_clustering':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")




                    ##### Ассоциативные правила web
                    elif self.algo_state.GetLabel() == 'asociative_rules_apriori':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'asociative_rules_aprioriTID':
                        minSupport = self.advanced_settings_float(self.settings_value_1.GetValue())
                        minConfidence = self.advanced_settings_float(self.settings_value_2.GetValue())
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            data_iter = io.Input.internet_read_csv(self.file_path_web())
                            items, rules = runApriori(data_iter, minSupport, minConfidence)
                            printResults(items, rules)

                    elif self.algo_state.GetLabel() == 'asociative_rules_aprioriHybrid':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'asociative_rules_DHP':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                    elif self.algo_state.GetLabel() == 'asociative_rules_PARTITION':
                        if self.file_type_check_web() == 'txt':
                            wx.MessageBox("Работа с txt файлами временно не поддерживается")
                        elif self.file_type_check_web() == 'csv':
                            wx.MessageBox("Работа с csv файлами временно не поддерживается")

                else:
                    wx.MessageBox("URL не указан или имеет неверный формат")

            elif self.radioBtn_random.GetValue():
                wx.MessageBox("Рандом временно недоступен")
        else:
            wx.MessageBox("Выберите алгоритм")


app = wx.App(False)
frame = MainWindow(None)
frame.Show()
app.MainLoop()