Введение в PyQt
===============

* PyQt - это инструмент для разработки графических интерфейсов, реализованный на языке Python и использующий библиотеку Qt.
* Если коротко - PyQt - это набор модулей и классов, каждый из которых отвечает за конкретную задачу, класс кнопки, класс выпадающего списка, класс текстового поля.
* Каждый класс содержит в себе набор функций, чтобы мы могли управлять этим граафическим элементом а так же менять его внешний вид. Например в классе кнопки есть функции, которые позволяют изменить текст кнопки, внешний вид, а так же определить реакцию, т.е. что должно произойти когда мы нажали на кнопку, провели над ней мышкой и т.д.
* С помощью Qt можно создавать абсолютно что угодно, браузеры, редакторы текстов, 3d игры, сложные приложения (как например Maya), программы на android OS и т.д.
* Интерфейс, написанный на PyQt - можно запустить на любой операционной системе, где есть python и PyQt, без каких-либо изменений. Так же его можно запустить как отдельную программу, не являющуюся частью Maya или 3d Max, Houdini и т.д.
* Поскольку Qt (еще этот инструмент называют фреймворком, т.е. что-то состоящие из огромного числа модулей и классов) - это очень продвинутый инстурмент, состоящий из огромнейшего числа модулей, он был разделен на основые модули, через которые мы можем получить доступ к определенным элементам. Например модуль QtWidgets отвечает за графические элементы - виджеты, которые мы видим на экране. QtCore отвечает за иной функционал, который так же важен, но уже не видим для обычных пользователей. QtNetwork отвечает за классы, связанные с сетевым программированием. В Qt очень много модулей, часть который никогда не понадобится, если только вы не решите сменить род деятельности и , например, стать программистами серверных приложений.
* Поскольку Maya построен полностью на Qt, у нее есть своя версия PyQt, которой могут пользоваться программисты Maya - она называется PySide. Чтобы начать пользоваться PySide - достаточно выполнить import PySide в Maya.
* В PyQt интерфейс состоит из виджетов (кнопки, списки, галочки, меню всякие), которые в свою очередь должны быть помещены в лэйауты (layout), своего рода зоны, в которых виджеты будут располагаться вертикально, либо горизонтально, либо в сетку. 
* Qt предоставляет большое количество готовых решений (Диалоговые окна с вопросом Да/Нет, диалоговые окна открытия/сохранения файла в файловой системе и т.д.) И большинство этих решений реализуется в Python небольшой командой. 
* Любой виджет Qt можно переделать на свой лад, и в дальнейшем использовать для своих нужд. 
* Иерархия виджетов в Qt создается следующим образом - Создается главный виджет, например Dialog (самый распространенный виджет), в него помещаются layouts, в которые в свою очередь могут быть помещены другие виджеты ... в которые могут быть помещены другие layouts и в них еще виджеты. И т.д. Однако принципиальное отличие layout в Qt от тех layout, которые мы создаем в MEL когда пишем на MEL интерфейс - в них трудно запутаться, с ними легко работать и создание интерфейсов превращается в креативный труд нежели чем в шаманские танцы с бубном в надежде заставить программу работать. 