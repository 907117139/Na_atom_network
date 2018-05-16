from flask import Flask, render_template, flash
from form import lambdaForm
import interpolation
from algorithm import compute_parameter

app = Flask(__name__)
app.config['SECRET_KEY'] = 'guess'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = lambdaForm()
    wave_number1 = "unknow"
    wave_number2 = "unknow"
    energy_level1 = "unknow"
    energy_level2 = "unknow"
    fixed_term = "unknow"
    delta = "unknow"
    n = "unknow"
    delta_l = "unknow"
    if form.validate_on_submit():
        lambda1 = form.lambda1.data
        lambda2 = form.lambda2.data
        if interpolation.n_error(lambda1,lambda2):
            # return render_template('n_error.html')
            flash('数据不合法')
            args_dict = {'form': form, 'wave_number1': wave_number1, 'wave_number2': wave_number2,
                         'energy_level1': energy_level1, 'energy_level2': energy_level2, 'fixed_term': fixed_term,
                         'delta': delta, 'n': n, 'delta_l': delta_l}
            return render_template('Natom_network.html', ** args_dict)
        else:
            args_dict = {'form': form}
            args_dict.update(compute_parameter(lambda1, lambda2))
    else:
        args_dict = {'form': form, 'wave_number1': wave_number1, 'wave_number2': wave_number2,
                     'energy_level1': energy_level1, 'energy_level2': energy_level2, 'fixed_term': fixed_term,
                     'delta': delta, 'n': n, 'delta_l': delta_l}
    return render_template('Natom_network.html', ** args_dict)


if __name__ == '__main__':
    app.run()