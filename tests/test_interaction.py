import time
from conftest import driver

from pages.interaction_page import SortablePage, SelectablePage, ResizablePage, DropPage, DraggablePage


class TestInteraction:
    class TestSortablePage:
        def test_sortable(self,driver):
            sortable_page= SortablePage(driver,'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_list()
            assert order_before != order_after

        def test_sortable_in_grid(self, driver):
            sortable_page = SortablePage(driver, 'https://demoqa.com/sortable')
            sortable_page.open()
            order_before, order_after = sortable_page.change_list_in_grid()
            assert order_before != order_after
    class TestSelectablePage:

        def test_selectable(self,driver):
            selectable =SelectablePage(driver,'https://demoqa.com/selectable')
            selectable.open()
            active_list=selectable.selected_list_item()
            active_grid = selectable.selected_grid_item()
            assert active_grid != ''
            assert active_list != ''

    class TestResizablePage:
        def test_check_size (self,driver):
            check_size= ResizablePage(driver,'https://demoqa.com/resizable')
            check_size.open()
            big_max_size, big_min_size= check_size.change_size_big_box()
            max_size, min_size = check_size.change_size_small_box()
            assert big_max_size == ('width: 500px; height: 300px;', 'width: 500px; height: 300px;') and big_min_size == ('width: 150px; height: 150px;', 'width: 150px; height: 150px;')
            assert max_size !=  min_size
    class TestDropPage:
        def test_simple_drop(self,driver):
            drop=DropPage(driver,'https://demoqa.com/droppable')
            drop.open()
            text = drop.drop_simple()
            assert text == 'Dropped!'

        def test_accept_drop(self,driver):
            drop=DropPage(driver,'https://demoqa.com/droppable')
            drop.open()
            text_not_acceotable = drop.drop_not_accept()
            text_acceptable  = drop.drop_accept()
            assert text_not_acceotable == 'Drop here'
            assert text_acceptable== 'Dropped!'


        def test_prevent_drop(self,driver):
            drop=DropPage(driver,'https://demoqa.com/droppable')
            drop.open()
            text_greedy_before, text_not_greedy_before,text_greedy_after,text_not_greedy_after =drop.drop_prevent_propogation()
            assert text_greedy_after =='Dropped!'
            assert text_not_greedy_after =='Dropped!'



        def test_revert_drop(self,driver):
            drop=DropPage(driver,'https://demoqa.com/droppable')
            drop.open()
            position_before, position_after = drop.drop_revert()
            position_will_not_before, position_will_not_after = drop.drop_not_revert()
            assert position_before != position_after
            assert position_will_not_before == position_will_not_after

    class TestDraggablePage:

        def test_check_simple(self,driver):
            check= DraggablePage(driver,'https://demoqa.com/dragabble')
            check.open()
            position_before, position_after= check.draggable1_check()
            assert  position_before != position_after

        def test_check_axis(self, driver):
            check = DraggablePage(driver, 'https://demoqa.com/dragabble')
            check.open()
            position_beforex, position_afterx,position_beforey, position_aftery = check.draggable_check_axis()
            assert position_beforex != position_afterx
            assert position_beforey != position_aftery






















