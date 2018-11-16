from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from .forms import DepartmentForm, UserAssignForm, RoleForm, BreedForm
from .. import db
from ..models import Department, User, Role, Breed


def check_admin():
    # prevent non-admins from accessing the page
    if not current_user.is_admin:
        abort(403)

@admin.route('/breeds', methods=['GET','POST'])
@login_required
def list_breeds():
    """
    List all breeds
    """
    check_admin()

    breeds = Breed.query.all()

    return render_template('admin/breeds/breeds.html',
                           breeds=breeds, title="Breeds")
@admin.route('/breeds/add', methods=['GET', 'POST'])
@login_required
def add_breed():
    """
    Add a breed to the database
    """
    check_admin()

    add_department = True

    form = BreedForm()
    if form.validate_on_submit():
        breed = Breed(name=form.name.data,
                      thcvalue=form.thcvalue.data,
                      outheight=form.outheight.data,
                      inheight=form.inheight.data)
        try:
            # add breed to the database
            db.session.add(breed)
            db.session.commit()
            flash('You have successfully added a new breed.')
        except:
            # in case breed name already exists
            flash('Error: breed smth already exists.')

        # redirect to breed page
        return redirect(url_for('admin.list_breeds'))

    # load breed template
    return render_template('admin/breeds/breed.html', action="Add",
                           add_breed=add_breed, form=form,
                           title="Add Department")


@admin.route('/breeds/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_breed(id):
    """
    Edit a breed
    """
    check_admin()

    add_breed = False

    breed = Breed.query.get_or_404(id)
    form = BreedForm(obj=breed)
    if form.validate_on_submit():
        breed.name=form.name.data
        breed.thcvalue=form.thcvalue.data
        breed.inheight=form.inheight.data
        breed.outheight=form.outheight.data
        db.session.commit()
        flash('You have successfully edited the breed.')

        # redirect to the departments page
        return redirect(url_for('admin.list_breeds'))

    form.name.data = breed.name
    form.thcvalue = breed.thcvalue
    form.inheight = breed.inheight
    form.outheight = breed.outheight
    return render_template('admin/breeds/breed.html', action="Edit",
                           add_breed=add_breed, form=form,
                           breed=breed, title="Edit breed")


@admin.route('/breeds/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_breed(id):
    """
    Delete a breed from the database
    """
    check_admin()

    breed = Breed.query.get_or_404(id)
    db.session.delete(breed)
    db.session.commit()
    flash('You have successfully deleted the breed.')

    # redirect to the breeds page
    return redirect(url_for('admin.list_breeds'))

    return render_template(title="Delete Breeds")


# Department Views


@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    """
    List all departments
    """
    check_admin()

    departments = Department.query.all()

    return render_template('admin/departments/departments.html',
                           departments=departments, title="Departments")


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Add a department to the database
    """
    check_admin()

    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data,
                                description=form.description.data)
        try:
            # add department to the database
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department.')
        except:
            # in case department name already exists
            flash('Error: department name already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_departments'))

    # load department template
    return render_template('admin/departments/department.html', action="Add",
                           add_department=add_department, form=form,
                           title="Add Department")


@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Edit a department
    """
    check_admin()

    add_department = False

    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the department.')

        # redirect to the departments page
        return redirect(url_for('admin.list_departments'))

    form.description.data = department.description
    form.name.data = department.name
    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")


@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """
    Delete a department from the database
    """
    check_admin()

    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the department.')

    # redirect to the departments page
    return redirect(url_for('admin.list_departments'))

    return render_template(title="Delete Department")


# Role Views


@admin.route('/roles')
@login_required
def list_roles():
    check_admin()
    """
    List all roles
    """
    roles = Role.query.all()
    return render_template('admin/roles/roles.html',
                           roles=roles, title='Roles')


@admin.route('/roles/add', methods=['GET', 'POST'])
@login_required
def add_role():
    """
    Add a role to the database
    """
    check_admin()

    add_role = True

    form = RoleForm()
    if form.validate_on_submit():
        role = Role(name=form.name.data,
                    description=form.description.data)

        try:
            # add role to the database
            db.session.add(role)
            db.session.commit()
            flash('You have successfully added a new role.')
        except:
            # in case role name already exists
            flash('Error: role name already exists.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    # load role template
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title='Add Role')


@admin.route('/roles/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    """
    Edit a role
    """
    check_admin()

    add_role = False

    role = Role.query.get_or_404(id)
    form = RoleForm(obj=role)
    if form.validate_on_submit():
        role.name = form.name.data
        role.description = form.description.data
        db.session.add(role)
        db.session.commit()
        flash('You have successfully edited the role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_roles'))

    form.description.data = role.description
    form.name.data = role.name
    return render_template('admin/roles/role.html', add_role=add_role,
                           form=form, title="Edit Role")


@admin.route('/roles/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_role(id):
    """
    Delete a role from the database
    """
    check_admin()

    role = Role.query.get_or_404(id)
    db.session.delete(role)
    db.session.commit()
    flash('You have successfully deleted the role.')

    # redirect to the roles page
    return redirect(url_for('admin.list_roles'))

    return render_template(title="Delete Role")


# Employee Views

@admin.route('/users')
@login_required
def list_users():
    """
    List all users
    """
    check_admin()

    users = User.query.all()
    return render_template('admin/users/users.html',
                           users=users, title='Employees')


@admin.route('/users/assign/<int:id>', methods=['GET', 'POST'])
@login_required
def assign_user(id):
    """
    Assign a department and a role to a user
    """
    check_admin()

    user = User.query.get_or_404(id)

    # prevent admin from being assigned a department or role
    if user.is_admin:
        abort(403)

    form = UserAssignForm(obj=user)
    if form.validate_on_submit():
        user.department = form.department.data
        user.role = form.role.data
        db.session.add(user)
        db.session.commit()
        flash('You have successfully assigned a department and role.')

        # redirect to the roles page
        return redirect(url_for('admin.list_employees'))

    return render_template('admin/users/user.html',
                           user=user, form=form,
                           title='Assign Employee')
