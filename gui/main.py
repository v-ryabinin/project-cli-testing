#!/usr/bin/python3
from fileinput import filename

import flet as ft

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import cli_test_project.copy as cliCopy
import cli_test_project.count_files as cliCount
import cli_test_project.delete as cliDelete


def main(page: ft.Page):
    page.title = "File Tools GUI"
    page.window.width = 600
    page.window.height = 600
    page.padding = 20
    page.theme_mode = ft.ThemeMode.LIGHT

    # copy
    copy_src_picker = ft.FilePicker()
    copy_dst_picker = ft.FilePicker()
    page.overlay.append(copy_src_picker)
    page.overlay.append(copy_dst_picker)
    copy_src_path = None
    copy_dst_path = None

    def on_copy_src_result(e: ft.FilePickerResultEvent):
        nonlocal copy_src_path
        if e.files:
            copy_src_path = e.files[0].path
            copy_src_field.value = copy_src_path
            copy_src_field.update()

    def on_copy_dst_result(e: ft.FilePickerResultEvent):
        nonlocal copy_dst_path
        nonlocal copy_src_path
        namefile = os.path.basename(copy_src_path)
        copy_dst_path = f"{e.path}\\{namefile}"
        copy_dst_field.value = copy_dst_path
        copy_dst_field.update()

    copy_src_picker.on_result = on_copy_src_result
    copy_dst_picker.on_result = on_copy_dst_result

    copy_src_field = ft.TextField(
        label="Src File",
        hint_text="Select src file...",
        read_only=False,
        width=400,
        tooltip="Path to the src file",
    )

    copy_dst_field = ft.TextField(
        label="Dst File",
        hint_text="Select dst file...",
        read_only=False,
        width=400,
        tooltip="Path to the dst file",
    )

    copy_src_button = ft.ElevatedButton(
        "Browse...",
        icon=ft.Icons.FOLDER_OPEN,
        on_click=lambda _: copy_src_picker.pick_files(dialog_title="Select src file", allow_multiple=False),
    )

    copy_dst_button = ft.ElevatedButton(
        "Browse...",
        icon=ft.Icons.FOLDER_OPEN,
        on_click=lambda _: copy_dst_picker.get_directory_path(dialog_title="Select dst file"),
    )

    copy_src_box = ft.Row([copy_src_field, copy_src_button])
    copy_dst_box = ft.Row([copy_dst_field, copy_dst_button])

    def copy():
        cliCopy.copy_file(copy_src_path, copy_dst_path)

    copy_button = ft.ElevatedButton(
        "Copy",
        icon=ft.Icons.COPY,
        on_click=lambda _: copy(),
    )

    copy_box = ft.Container(
        content=ft.Column([copy_src_box, copy_dst_box, copy_button]),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        border=ft.border.all(1),
        border_radius=1,
    )

    # delete
    delete_picker = ft.FilePicker()
    page.overlay.append(delete_picker)
    delete_path = None

    def on_delete_result(e: ft.FilePickerResultEvent):
        nonlocal delete_path
        if e.files:
            delete_path = e.files[0].path
            delete_field.value = delete_path
            delete_field.update()

    delete_picker.on_result = on_delete_result

    delete_field = ft.TextField(
        label="Delete File",
        hint_text="Select delete file...",
        read_only=False,
        width=400,
        tooltip="Path to the delete file",
    )

    delete_path_button = ft.ElevatedButton(
        "Browse...",
        icon=ft.Icons.FOLDER_OPEN,
        on_click=lambda _: delete_picker.pick_files(dialog_title="Select delete file", allow_multiple=False),
    )

    delete_box = ft.Row([delete_field, delete_path_button])

    delete_button = ft.ElevatedButton(
        "Delete",
        icon=ft.Icons.DELETE,
        on_click=lambda _: cliDelete.delete_file(delete_path),
    )

    delete_box = ft.Container(
        content=ft.Column([delete_box, delete_button]),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        border=ft.border.all(1),
        border_radius=1,
    )

    # count
    count_picker = ft.FilePicker()
    page.overlay.append(count_picker)
    count_path = None

    def on_count_result(e: ft.FilePickerResultEvent):
        nonlocal count_path
        count_path = e.path
        count_field.value = count_path
        count_field.update()

    count_picker.on_result = on_count_result

    count_field = ft.TextField(
        label="Count File",
        hint_text="Select count file...",
        read_only=False,
        width=400,
        tooltip="Path to the count file",
    )

    count_path_button = ft.ElevatedButton(
        "Browse...",
        icon=ft.Icons.FOLDER_OPEN,
        on_click=lambda _: count_picker.get_directory_path(dialog_title="Select count file"),
    )

    count_box = ft.Row([count_field, count_path_button])

    count = 0
    count_text = ft.Text(f"Count = {count}")

    def counter():
        count = cliCount.count_files(count_path)
        count_text.value = f"Count = {count}"

    count_button = ft.ElevatedButton(
        "Count",
        icon=ft.Icons.COUNTERTOPS,
        on_click=lambda _: counter(),
    )

    count_box = ft.Container(
        content=ft.Column([count_box, ft.Row([count_button, count_text])]),
        margin=10,
        padding=10,
        alignment=ft.alignment.center,
        border=ft.border.all(1),
        border_radius=1,
    )

    page.add(
        ft.Column(
            [
                copy_box,
                delete_box,
                count_box,
            ]
        )
    )


if __name__ == "__main__":
    ft.app(target=main)
