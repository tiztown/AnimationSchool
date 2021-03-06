Введение в PyQt
===============

* PyQt - это инструмент для разработки графических интерфейсов, реализованный на языке Python и использующий библиотеку Qt.
* Если коротко - PyQt - это набор модулей и классов, каждый из которых отвечает за конкретную задачу, класс кнопки, класс выпадающего списка, класс текстового поля.
* Каждый класс содержит в себе набор функций, чтобы мы могли управлять этим граафическим элементом а так же менять его внешний вид. Например в классе кнопки есть функции, которые позволяют изменить текст кнопки, внешний вид, а так же определить реакцию, т.е. что должно произойти когда мы нажали на кнопку, провели над ней мышкой и т.д.
* С помощью Qt можно создавать абсолютно что угодно, браузеры, редакторы текстов, 3d игры, сложные приложения (как например Maya), программы на android OS и т.д.
* Интерфейс, написанный на PyQt - можно запустить на любой операционной системе, где есть python и PyQt, без каких-либо изменений. Так же его можно запустить как отдельную программу, не являющуюся частью Maya или 3d Max, Houdini и т.д.
* Поскольку Qt (еще этот инструмент называют фреймворком, т.е. что-то состоящие из огромного числа модулей и классов) - это очень продвинутый инстурмент, состоящий из огромнейшего числа модулей, он был разделен на основые модули, через которые мы можем получить доступ к определенным элементам. Например модуль **QtWidgets** отвечает за графические элементы - виджеты, которые мы видим на экране. **QtCore** отвечает за иной функционал, который так же важен, но уже не видим для обычных пользователей. **QtNetwork** отвечает за классы, связанные с сетевым программированием. В Qt очень много модулей, часть который никогда не понадобится, если только вы не решите сменить род деятельности и , например, стать программистами серверных приложений.
* Поскольку Maya построена полностью на Qt, у нее есть своя версия PyQt, которой могут пользоваться программисты Maya - она называется PySide. Чтобы начать пользоваться PySide - достаточно выполнить import PySide в Maya.
* В PyQt интерфейс состоит из виджетов (кнопки, списки, галочки, меню всякие), которые в свою очередь должны быть помещены в лэйауты (layout), своего рода зоны, в которых виджеты будут располагаться вертикально, либо горизонтально, либо в сетку. 
* Qt предоставляет большое количество готовых решений (Диалоговые окна с вопросом Да/Нет, диалоговые окна открытия/сохранения файла в файловой системе и т.д.) И большинство этих решений реализуется в Python небольшой командой. 
* Любой виджет Qt можно переделать на свой лад, и в дальнейшем использовать для своих нужд. 
* Иерархия виджетов в Qt создается следующим образом - Создается главный виджет, например Dialog (самый распространенный виджет), в него помещаются layouts, в которые в свою очередь могут быть помещены другие виджеты ... в которые могут быть помещены другие layouts и в них еще виджеты. И т.д. Однако принципиальное отличие layout в Qt от тех layout, которые мы создаем в MEL когда пишем на MEL интерфейс - в них трудно запутаться, с ними легко работать и создание интерфейсов превращается в креативный труд нежели чем в шаманские танцы с бубном в надежде заставить программу работать. 
* Начиная с версии Maya2017 - разработчики включили в дистрибутив Maya новые версии питона (версия 3) и PySide (версия 2). У этих и предыдущих версий есть много отличий. Например, теперь мы импортируем PySide2 а не PySide как в версиях Maya2016 и ранее. Но главное отличие - это то, что теперь все графические элементы создаются через модуль QtWidgets (ранее они создавались через QtGui). И для многих компаний это стало проблемой т.к. были те, кто работали в Maya2016, и те кто работали в Maya2017, и для программистов написание программ превратилось в головную боль, пока парни из Disney не написали дополнительный модуль Qt.py, который позволял писать интерфейсы и больше не заботиться о версии Maya. Единственное требование было - чтобы отныне все программы писались на новый лад (как под версию PySide2), и эти программы могли с легкостью запускаться в ранних версиях Maya. Если коротко о том, что происзодит внутри Qt.py - там весь новый синтаксис автоматически заменяется на старый, если версия Maya ниже 2017


Практические заметки
--------------------

* Минимальный набор команд, чтобы создать Qt окно

.. code-block:: python

  from PySide2 import QtWidgets

  class MyDialog(QtWidgets.QDialog):

      def __init__(self, parent = None):

          super(MyDialog, self).__init__() #run __init__ from inherited class - QDialog

          # our class MyDialog inherits everything from QDialog
          # it is enough to run our UI


  myUi = MyDialog() # create an instance of our dialog class
  myUi.show() # show the dialog

В данном коде мы сначала проимпортировали необходимые модули из PySide2. При создании нашего класса окна мы унаследовали весь функционал и все свойства диалогового окна Qt. Делается это для того, чтобы нам осталось лишь внести нужные в класс изменения и получить то окно, которое мы хотим.

В методе __init__ мы использовали аттрибут parent = None. Этот аттрибут присутствует и у класса QDialog.__init__, и отвечает он за родительское окно. В программировании интерфейсов есть такое понятие как иерархия окон. Т.е. если у нас есть главное окно (самое верхрее по иерархии - например программа Maya), то любое создаваемое дочернее окно будет всегда находиться поверх родительского окна, а иногда и блокировать его. Однако, поскольку parent = None, значит у нашего окна нет родительского окна. А потому, когд мы кликнем случайно мышкой в Майку, наше окно исчезнет за главным окном Майа.

Когда мы запустили super(MyDialog, self).__init__() - мы фактически выполнили __init__ класса QDialog, и таким образом наполнили наше диалоговое окно всеми свойствами окна QDialog со занчениями по умолчанию. Если мы запустим код, то увидим, что 
окно имеет определенный размер, название окна Maya-2018 (по крайней мере у меня так). Я могу легко поменять размер окна если потяну за гранницу. Ну и окно не имеет никаких элементов. Потому что мы их и не создали еще. Но вся суть в Qt в том, чтобы взять базовое окно, и переделать его так как нам необходимо.

Свойства виджетов
-----------------

Теперь внесем первые изменения в наш класс окна.

.. code-block:: python

  import maya.cmds as cmds
  from PySide2 import QtWidgets, QtGui, QtCore

  class MyDialog(QtWidgets.QDialog):

      def __init__(self, parent = None):

          super(MyDialog, self).__init__() #run __init__ from inherited class - QDialog

          self.setWindowTitle("My new dialog") #window title
          self.setObjectName("mynewdlg") # the same as ID - should always be unique and no spaces in-between
          self.setMinimumSize(600,400) # now we can't resize window to make it less than 600px width and 400px height
          self.setMaximumSize(1000,800) # the same - we can't make it larger than 1000px width and 800px height


  # here we just make sure that any window that has "ObjectName = mynewdlg" is deleted 
  if cmds.window("mynewdlg", q=1, exists=1):
      cmds.deleteUI("mynewdlg")

  myUi = MyDialog() # create an instance of our dialog class
  myUi.show() # show the dialog
 
Здесь мы внесли небольшие изменения в наше окно. Самым важным изменением стало изменение идентификатора окна с помощью **setObjectName()**. У каждого элемента - кнопки, галочки, слайдера или целого окна - всегда должно быть уникальное имя. Это является хорошим тоном программирования, а так же может использоваться в каких-то целях.

Мы так же добавили функцию MEL - cmds.deleteUI, которая удаляет все окна, у которых идентификатор равняется "mynewdlg", чтобы избежать проблемы создания нескольких окон одновременно.


Создание элементов UI - Layouts
-------------------------------

Прежде чем добавлять в интерфейс какие-либо элементы, следует понимать что такое Layout. Layout - это особый объект (можно думать о нем как о коробке), в который помещаются виджеты, например кнопки, списки, меню. Причем, от того, какой layout мы использовали - виджеты будут располагаться в нем либо горизонтально, либо вертикально, либо как в сетке - в заданной позиции. 

Есть несколько видов layout - **QHBoxLayout** (элемента расположены в нем строго горизонтально), **QVBoxLayout** (элементы расположены вертикально), **QGridLayout** (элементы расположены по сетке - с указанием колонки и ряда) и **QFormLayout** (где элементы расположены в две колонки - обычно это какое то слово и поле куда нужно что-то ввести, как на сайте во время регистрации).

Как правило у нас изначально в интерфейсе нет никаких layout, а значит мы не можем в главное окно добавить виджеты. Как правило то, какие Layout добавлять - решать программисту. Причем в каждый Layout можно давить другие layouts, и в них еще layouts. 

Рассмотрим пример, когда мы добавим QVBoxLayout, чтобы наши элементы UI располагались вертикально.

.. code-block:: python

  class MyDialog(QtWidgets.QDialog):

    def __init__(self, parent = None):
        super(MyDialog, self).__init__() #run __init__ from inherited class - QDialog
        self.setWindowTitle("My new dialog") 
        self.setObjectName("mynewdlg") 

        self.main_layout = QtWidgets.QVBoxLayout() # create Qt Vertical Box Layout

        self.setLayout(self.main_layout) # Here we set self.main_layout as main layout for MyDialog widget.
        
Теперь мы можем в self.main_layout добавлять различные виджеты либо другие layouts.

.. code-block:: python

  class MyDialog(QtWidgets.QDialog):

      def __init__(self, parent = None):
          super(MyDialog, self).__init__() #run __init__ from inherited class - QDialog
          self.setWindowTitle("My new dialog") 
          self.setObjectName("mynewdlg") 

          self.main_layout = QtWidgets.QVBoxLayout() # create Qt Vertical Box Layout
          self.setLayout(self.main_layout) # Here we set self.main_layout as main layout for MyDialog widget.

          self.button_01 = QtWidgets.QPushButton("Button 01") # create button widget
          self.button_02 = QtWidgets.QPushButton("Button 02")
          self.button_03 = QtWidgets.QPushButton("Button 03")

          self.main_layout.addWidget(self.button_01) # add button widget to our layout
          self.main_layout.addWidget(self.button_02)
          self.main_layout.addWidget(self.button_03)
          
          # if we want to add new layout to self.main_layout
          self.horizontal_layout = QtWidgets.QHBoxLayout() # create Qt Horizontal Box Layout
          
          self.main_layout.addLayout(self.horizontal_layout) # our new layout is located below the buttons
          
          #now we can add new buttons to a new layout and the will be located horizontally below other buttons
          
          self.h_button_1 = QtWidgets.QPushButton("Horz Button 01")
          self.h_button_2 = QtWidgets.QPushButton("Horz Button 02")
          self.h_button_3 = QtWidgets.QPushButton("Horz Button 03")
          
          self.horizontal_layout.addWidget(self.h_button_1)
          self.horizontal_layout.addWidget(self.h_button_2)
          self.horizontal_layout.addWidget(self.h_button_3)

