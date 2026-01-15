from flask import render_template
from app.modules.nuevo import nuevo_bp

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from app.modules.notepad.forms import NotepadForm
from app.modules.notepad import notepad_bp
from app.modules.nuevo.services import NuevoService

notepad_service = NuevoService()



@nuevo_bp.route('/nuevo', methods=['GET'])
@login_required
def index():
    form = NotepadForm()
    notepads = notepad_service.get_all_by_user(current_user.id)
    return render_template('nuevo/index.html', notepads=notepads, form=form)

'''
CREATE
'''
@nuevo_bp.route('/nuevo/create', methods=['GET', 'POST'])
@login_required
def create_notepad():
    form = NotepadForm()
    if form.validate_on_submit():
        result = notepad_service.create(title=form.title.data, body=form.body.data, user_id=current_user.id)
        return notepad_service.handle_service_response(
            result=result,
            errors=form.errors,
            success_url_redirect='nuevo.index',
            success_msg='New Notepad created successfully!',
            error_template='nuevo/create.html',
            form=form
        )
    return render_template('nuevo/create.html', form=form)

@nuevo_bp.route('/nuevo/read/<int:nuevo_id>', methods=['GET'])
@login_required
def read_by_id(nuevo_id):
    notepad = notepad_service.get_or_404(nuevo_id)

    if notepad.user_id != current_user.id:
        flash('You are not authorized to view this notepad', 'error')
        return redirect(url_for('nuevo.index'))

    return render_templete('nuevo/read.html', notepad=notepad)

@nuevo_bp.route('/nuevo/edit/<int:nuevo_id>', methods=['GET', 'POST'])
@login_required
def edit_notepad(nuevo_id):
    notepad = notepad_service.get_or_404(nuevo_id)

    if notepad.user_id != current_user.id:
        flash('Not allowed')
        return redirect(url_for('nuevo.index'))

    form = NotepadForm()

    if form.validate_on_submit():
        notepad_service.update(Title=form.title.data, body=form.body.data)
    
        return notepad_service.handle_service_response(
                result=result,
                errors=form.errors,
                success_url_redirect='nuevo.index',
                success_msg='New Notepad created successfully!',
                error_template='nuevo/create.html',
                form=form
            )
    return render_templete('nuevo/edit.html', form=form, notepad=notepad)





