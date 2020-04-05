from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
from data import *
from Common_Object_def import *


class MP2X_L_Demand(QWidget):
    def __init__(self, Panel_ID, nodename, Destination):
        super(MP2X_L_Demand, self).__init__()

        self.id = Panel_ID
        self.nodename = nodename
        self.Destination = Destination
        self.uppernum = str(int(Panel_ID) + 1)
        
        
        
        #self.setObjectName("self")
        self.setFixedSize(116, 521)
        #self.resize(116, 521)
        self.client1 = customlabel(self, self.nodename, self.id, 1)
        self.client1.setGeometry(QRect(30, 120, 21, 71))
        self.client1.setText("")
        self.client1.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client1.setObjectName("client1")  

        self.client2 = customlabel(self, self.nodename, self.id, 2)
        self.client2.setGeometry(QRect(50, 120, 21, 71))
        self.client2.setText("")
        self.client2.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client2.setObjectName("client2")  

        self.client3 = customlabel(self, self.nodename, self.id, 3)
        self.client3.setGeometry(QRect(30, 160, 21, 71))
        self.client3.setText("")
        self.client3.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client3.setObjectName("client3") 

        self.client4 = customlabel(self, self.nodename, self.id, 4)
        self.client4.setGeometry(QRect(50, 160, 21, 71))
        self.client4.setText("")
        self.client4.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client4.setObjectName("client4")
        
        
        self.client5 = customlabel(self, self.nodename, self.id, 5)
        self.client5.setGeometry(QRect(30, 200, 21, 71))
        self.client5.setText("")
        self.client5.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client5.setObjectName("client5") 

        self.client6 = customlabel(self, self.nodename, self.id, 6)
        self.client6.setGeometry(QRect(50, 200, 21, 71))
        self.client6.setText("")
        self.client6.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client6.setObjectName("client6") 

        self.client7 = customlabel(self, self.nodename, self.id, 7)
        self.client7.setGeometry(QRect(30, 240, 21, 71))
        self.client7.setText("")
        self.client7.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client7.setObjectName("client7") 

        self.client8 = customlabel(self, self.nodename, self.id, 8)
        self.client8.setGeometry(QRect(50, 240, 21, 71))
        self.client8.setText("")
        self.client8.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client8.setObjectName("client8")  

        self.client9 = customlabel(self, self.nodename, self.id, 9)
        self.client9.setGeometry(QRect(30, 280, 21, 71))
        self.client9.setText("")
        self.client9.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client9.setObjectName("client9") 

        self.client10 = customlabel(self, self.nodename, self.id, 10)
        self.client10.setGeometry(QRect(50, 280, 21, 71))
        self.client10.setText("")
        self.client10.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client10.setObjectName("client10") 

        self.client11 = customlabel(self, self.nodename, self.id, 11)
        self.client11.setGeometry(QRect(30, 320, 21, 71))
        self.client11.setText("")
        self.client11.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client11.setObjectName("client11") 

        self.client12 = customlabel(self, self.nodename, self.id, 12)
        self.client12.setGeometry(QRect(50, 320, 21, 71))
        self.client12.setText("")
        self.client12.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client12.setObjectName("client12") 

        self.client13 = customlabel(self, self.nodename, self.id, 13)
        self.client13.setGeometry(QRect(30, 360, 21, 71))
        self.client13.setText("")
        self.client13.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client13.setObjectName("client13") 

        self.client14 = customlabel(self, self.nodename, self.id, 14)
        self.client14.setGeometry(QRect(50, 360, 21, 71))
        self.client14.setText("")
        self.client14.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client14.setObjectName("client14")
        
        
        self.client15 = customlabel(self, self.nodename, self.id, 15)
        self.client15.setGeometry(QRect(30, 400, 21, 71))
        self.client15.setText("")
        self.client15.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client15.setObjectName("client15") 

        self.client16 = customlabel(self, self.nodename, self.id, 16)
        self.client16.setGeometry(QRect(50, 400, 21, 71))
        self.client16.setText("")
        self.client16.setPixmap(QPixmap(os.path.join("MP2X_Demand","client.png")))
        self.client16.setObjectName("client16") 

        self.line1 = QLabel(self)
        self.line1.setGeometry(QRect(30, 100, 41, 31))
        self.line1.setText("")
        self.line1.setPixmap(QPixmap(os.path.join("MP2X_Demand","line2.png")))
        self.line1.setObjectName("line1") 

        self.line2 = QLabel(self)
        self.line2.setGeometry(QRect(50, 100, 51, 31))
        self.line2.setText("")
        self.line2.setPixmap(QPixmap(os.path.join("MP2X_Demand","line2.png")))
        self.line2.setObjectName("line2")
        
        self.upper_socket = QLabel(self)
        self.upper_socket.setGeometry(QRect(20, -20, 41, 81))
        self.upper_socket.setText("")
        self.upper_socket.setPixmap(QPixmap(os.path.join("MP2X_Demand","socket1.png")))
        self.upper_socket.setObjectName("upper_soclet") 

        self.socket = QLabel(self)
        self.socket.setGeometry(QRect(20, 470, 55, 61))
        self.socket.setText("")
        self.socket.setPixmap(QPixmap(os.path.join("MP2X_Demand","socket2.png")))
        self.socket.setObjectName("socket") 

        self.title = QLabel(self)
        self.title.setGeometry(QRect(70, 0, 55, 91))
        self.title.setText("")
        self.title.setPixmap(QPixmap(os.path.join("MP2X_Demand","title2.png")))
        self.title.setObjectName("title")

        QMetaObject.connectSlotsByName(self)

        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.setAcceptDrops(True)
    
    def contextMenuEvent(self, event):
        from BLANK_Demand.BLANK_Demand import BLANK_Demand
        ContextMenu = QMenu(self)
        CloseAction = ContextMenu.addAction("Close Panel")
        RefreshAction = ContextMenu.addAction(" Refresh ")
            
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == CloseAction:

            Data["DemandPanel_" + self.id].setWidget(BLANK_Demand(self.id ,  self.nodename, self.Destination))
            Data["DemandPanel_" + self.uppernum].setWidget(BLANK_Demand(self.id ,  self.nodename, self.Destination))

            # undoing every service or lightpath that is created in this panel
            if not(DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity) != [0, 0]:

                for i in range(len(DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity)):
                    if DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[i] != 0:
                        ids = [DemandTabDataBase["Panels"][self.nodename][self.id].DemandIdList[i], DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList[i]]
                        type = DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[i]

                        self.modify_ServiceList(ids, self.nodename, self.Destination, "add", type)

                LineServiceId = DemandTabDataBase["Panels"][self.nodename][self.id].LineServiceIdList

                if LineServiceId[0] != None:

                    self.modify_LightPathList(LineServiceId[0], self.nodename, self.Destination, mode="delete", type="MP2X Line")

                #Network.Lightpath.update_id(-1)
            DemandTabDataBase["Panels"][self.nodename].pop(self.id)
            DemandTabDataBase["Panels"][self.nodename].pop(self.uppernum)
        
        if action == RefreshAction:
            # TODO: recalculate line capacity
            pass
    
    def modify_groom_out_10(self, mp2x_line_id, Source, Destination, mode = "add", type = None):

        if mode == "add":
            DemandTabDataBase["Lightpathes"][(Source, Destination)][id] = "%s # %s" %(id, type)
        
        if mode == "delete":
            for Des in DemandTabDataBase["Source_Destination"][Source]:
                if id in DemandTabDataBase["Services"][(Source, Destination)]:
                    DemandTabDataBase["Lightpathes"][(Source, Destination)].pop(id)
        
        Data["ui"].update_Demand_lightpath_list()
    
    def modify_ServiceList(self, ids, source, destination, mode = "delete", type = None):

        key = (ids[0] , ids[1])
        if mode == "delete":
            DemandTabDataBase["Services"][(source, destination)].pop(key)
            
        elif mode == "add":
            DemandTabDataBase["Services"][(source, destination)][key] = "[%s , %s] # %s" % (ids[0], ids[1], type)
            
        Data["ui"].UpdateDemand_ServiceList()


class customlabel(QLabel):
    Stateflag = 0           # this flag shows that this panel is on or off
    def __init__(self, parent, nodename, Destination, ID, ClientNum , LineVar_1, LineVar_2):
        super().__init__(parent)
        self.nodename = nodename
        self.id = ID
        self.Destination = Destination
        self.LineVar_1 = LineVar_1
        self.LineVar_2 = LineVar_2
        self.ClientNum = ClientNum - 1  # because list indices starts with 0
        self.setAcceptDrops(True)

        self.BWDict = {"E1": 58.84 / 1024, "STM_1_Electrical": 155.52 / 1024, "STM_1_Optical": 155.52 / 1024, "STM_4": 622.08 / 1024, "STM_16": 2.49}
    
    def dragEnterEvent(self, event):
        e = event.mimeData()
        model = QStandardItemModel()
        model.dropMimeData(event.mimeData(), Qt.CopyAction, 0,0, QModelIndex())
        dragtext = model.item(0,0).text()
        UserData = model.item(0).data(Qt.UserRole)
        """ servicetype = dragtext.split("*")[1]
        servicetype = servicetype.strip() """
        self.allowedservices = ["E1", "STM_1_Electrical", "STM_1_Optical", "STM_4", "STM_16"]
        """ dragtext = dragtext.split("#")
        servicetype = dragtext[1].strip()
        ids = list(dragtext[0].strip())
        ids = [ids[1], ids[-2]] """
        servicetype = dragtext.strip()
        ids = [UserData["DemandId"], UserData["ServiceId"]]
        if servicetype in self.allowedservices:
            #self.setPixmap(QPixmap(os.path.join("MP2D_panel", "client_green.png")))
            Line_1_old_capacity = DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0]
            Line_2_old_capacity = DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1]
            DropCapacity = self.BWDict[self.servicetype]

            # checking wheater lines have enough capacity or not
            if Line_1_old_capacity + DropCapacity < 10 or Line_2_old_capacity + DropCapacity < 10:

                self.setPixmap(QPixmap(os.path.join("MP2X_Demand", "client_green.png")))
                event.accept()

        else:
            self.setPixmap(QPixmap(os.path.join("MP2X_Demand", "client_red.png")))
        

        super(customlabel,self).dragEnterEvent(event)
    

    def dragLeaveEvent(self, event):
        self.setPixmap(QPixmap(os.path.join("MP2X_Demand", "client.png")))

    def dropEvent(self, event):
        event.accept()
        e = event.mimeData()
        model = QStandardItemModel()
        model.dropMimeData(event.mimeData(), Qt.CopyAction, 0,0, QModelIndex())
        dragtext = model.item(0,0).text()
        UserData = model.item(0).data(Qt.UserRole)

        
        servicetype = dragtext.strip()


        if servicetype in self.allowedservices:

            self.servicetype = servicetype
            self.ids = (UserData["DemandId"], UserData["ServiceId"])            # ids : [ serviceId, DemandId ]
            
            self.setToolTip(DemandTabDataBase["Services_static"][self.nodename][self.ids].toolTip())

            # DemandTabDataBase["Panels"][self.nodename][self.id].add_client(self.ClientNum, servicetype)
            Line_1_old_capacity = DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0]
            Line_2_old_capacity = DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1]

            # updating ClientsCapacity in panel object
            DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum] = servicetype

            ServiceListLen = len(DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList)
            if self.ClientNum >= ServiceListLen:
                for i in range(ServiceListLen - self.ClientNum + 1):
                    DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList.append(None)

            # updating service id and demand id in panel object 
            DemandTabDataBase["Panels"][self.nodename][self.id].ServiceIdList[self.ClientNum] = self.ids[1]
            DemandTabDataBase["Panels"][self.nodename][self.id].DemandIdList[self.ClientNum] = self.ids[0]


            
            DropCapacity = self.BWDict[self.servicetype]
            

            self.modify_ServiceList(ids= self.ids,
                                    source= self.nodename,
                                    destination= self.Destination,
                                    mode= "delete")

            # check if line 1 in on or not
            if Line_1_old_capacity == 0:

                # updating line 1 capacity
                DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0] += DropCapacity

                # updating Line_1_ServiceIdList
                DemandTabDataBase["Panels"][self.nodename][self.id].Line_1_ServiceIdList.append(self.ids[1])
                
                # creating new groom out 10
                Data["NetworkObj"].add_groom_out_10(Source= self.nodename,
                                                    Destination= self.Destination,
                                                    DemandId= self.ids[1],
                                                    Capacity= self.BWDict[self.servicetype],
                                                    ServiceIdDict= [self.ids[0]])

                GroomOutId = max(Data["NetworkObj"].GroomOut10Dict.keys())

                # updating LineIdList in panel object
                DemandTabDataBase["Panels"][self.nodename][self.id].LineIdList[0] = GroomOutId

                self.modify_GroomOut10List(id= GroomOutId,
                                            Source= self.nodename,
                                            Destination= self.Destination,
                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0],
                                            mode= "add",
                                            type= "GroomOut10",
                                            PanelId= self.id)
                
                # setting line port tooltip                                        
                self.LineVar_1.setToolTip(DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId].toolTip())

            elif Line_1_old_capacity + DropCapacity < 10 :
                
                # updating line 1 capacity
                DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0] += DropCapacity

                # updating Line_1_ServiceIdList
                DemandTabDataBase["Panels"][self.nodename][self.id].Line_1_ServiceIdList.append(self.ids[1])

                GroomOutId = DemandTabDataBase["Panels"][self.nodename][self.id].LineIdList[0]

                ServiceIdList = [self.ids[1]]
                Data["NetworkObj"].GroomOut10Dict[GroomOutId].ServiceIdList.extend(ServiceIdList)

                # updating LightPath ListWidgetItem Capacity
                self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId],
                                                        Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[0])

                # setting line port tooltip                                        
                self.LineVar_1.setToolTip(DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId].toolTip())
            
            elif Line_2_old_capacity == 0:

                # updating line 2 capacity
                DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1] += DropCapacity

                # updating Line_2_ServiceIdList
                DemandTabDataBase["Panels"][self.nodename][self.id].Line_2_ServiceIdList.append(self.ids[1])

                # creating new groom out 10
                Data["NetworkObj"].add_groom_out_10(Source= self.nodename,
                                                    Destination= self.Destination,
                                                    DemandId= self.ids[1],
                                                    Capacity= self.BWDict[self.servicetype],
                                                    ServiceIdDict= [self.ids[0]])

                GroomOutId = max(Data["NetworkObj"].GroomOut10Dict.keys())

                # updating LineIdList in panel object
                DemandTabDataBase["Panels"][self.nodename][self.id].LineIdList[1] = GroomOutId

                self.modify_GroomOut10List(id= GroomOutId,
                                            Source= self.nodename,
                                            Destination= self.Destination,
                                            Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1],
                                            mode= "add",
                                            type= "GroomOut10",
                                            PanelId= self.id)
                
                # setting line port tooltip                                        
                self.LineVar_2.setToolTip(DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId].toolTip())
            
            else:

                # updating line 2 capacity
                DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1] += DropCapacity

                # updating Line_2_ServiceIdList
                DemandTabDataBase["Panels"][self.nodename][self.id].Line_2_ServiceIdList.append(self.ids[1])

                GroomOutId = DemandTabDataBase["Panels"][self.nodename][self.id].LineIdList[1]

                ServiceIdList = [self.ids[1]]
                Data["NetworkObj"].GroomOut10Dict[GroomOutId].ServiceIdList.extend(ServiceIdList)


                # updating LightPath ListWidgetItem Capacity
                self.Update_LineListWidgetItem_Tooltip( Item= DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId],
                                                        Capacity= DemandTabDataBase["Panels"][self.nodename][self.id].LinesCapacity[1])

                # setting line port tooltip                                        
                self.LineVar_2.setToolTip(DemandTabDataBase["GroomOut10"][(self.nodename, self.Destination)][GroomOutId].toolTip())


            # NOTE: be Careful !!!!!
            self.setAcceptDrops(False)  
        else:
            self.setPixmap(QPixmap(os.path.join("MP2X_Demand", "client.png")))

    def contextMenuEvent(self, event):
        ContextMenu = QMenu(self)
        ClearAction = ContextMenu.addAction("..Clear Socket..")
        
        action = ContextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == ClearAction:
            if DemandTabDataBase["Panels"][self.nodename][self.id].ClientsCapacity[self.ClientNum] != 0:
                self.setToolTip("")
                
                DemandTabDataBase["Panels"][self.nodename][self.id].del_client(self.ClientNum)
                self.setPixmap(QPixmap(os.path.join("MP2X_Demand", "client.png")))
                self.setAcceptDrops(True)
                self.modify_ServiceList(self.ids, self.nodename, self.Destination, mode = "add", type = servicetype)

    

    def Update_LineListWidgetItem_Tooltip(self, Item, Capacity):       
        
        UserData = Item.data(Qt.UserRole)
        #UserData = {"LightPathId":id, "Source":Source, "Destination":Destination, "Capacity":Capacity, "Type": type}
        UserData["Capacity"] = Capacity
        Item.setData(Qt.UserRole, UserData)
        Item.setToolTip(f"Source: {UserData['Source']}\nDestination: {UserData['Destination']}\nCapacity: {Capacity}\nType: {UserData['Type']}")

    def modify_ServiceList(self, ids, source, destination, mode = "delete", type = None):
        

        key = (int(ids[0]) , int(ids[1]))
        if mode == "delete":
            DemandTabDataBase["Services"][(source, destination)].pop(key)

            # statement bellow checks for removing notification
            x = 0
            for dest in DemandTabDataBase["Source_Destination"][source]["DestinationList"]:
                if DemandTabDataBase["Services"][(source, dest)]:
                    x = 1
                    break
            if x == 0:        
                Data["ui"].set_failed_nodes_default(source)
            
        elif mode == "add":
            DemandTabDataBase["Services"][(source, destination)][key] = None
            
        Data["ui"].UpdateDemand_ServiceList()
    
    def modify_GroomOut10List(self, id, Source, Destination, Capacity = None, mode = "add", type = None, PanelId = None):

        if mode == "add":
            #DemandTabDataBase["Lightpathes"][(Source, Destination)][id] = "%s # %s" %(id, type)
            item = QListWidgetItem(type, Data["GroomOu10_list"])
            UserData = {"GroomOut10d":id, "Source":Source, "Destination":Destination, "Capacity":Capacity, "Type": type, "PanelId": PanelId}
            item.setToolTip(f"Source: {Source}\nDestination: {Destination}\nCapacity: {Capacity}\nType: {type}")
            item.setData(Qt.UserRole, UserData)
            item.setTextAlignment(Qt.AlignCenter)

            DemandTabDataBase["GroomOut10"][(Source, Destination)][id] = item
        
        if mode == "delete":
            # deleting desired lightpath from database
            DemandTabDataBase["GroomOut10"][(Source, Destination)].pop(id)

            # correcting upper lightpath id's 
            for Des in DemandTabDataBase["Source_Destination"][Source]["DestinationList"]:
                for UpperId in sorted(list(DemandTabDataBase["GroomOut10"][(Source, Des)].keys())):
                    if UpperId > id:
                        DemandTabDataBase["GroomOut10"][(Source, Des)][UpperId - 1] = DemandTabDataBase["GroomOut10"][(Source, Des)].pop(UpperId)
                        UserData = DemandTabDataBase["GroomOut10"][(Source, Des)][UpperId - 1].data(Qt.UserRole)
                        UserData["GroomOut10Id"] -= 1
                        DemandTabDataBase["GroomOut10"][(Source, Des)][UpperId - 1].setData(Qt.UserRole, UserData) 
 
        Data["ui"].update_Demand_groomout10_list()