from sklearn.metrics import roc_auc_score
from Predict import *
import Evaluations as ev

#test_file,predict_file

def Auc_df():
    test_df = pd.read_csv("vdjdb_test_with_sign.csv")
    predict_df = pd.read_csv("dummy_results_to_auc.csv")
    y = test_df["Sign"]
    y_hat = predict_df["Score"]
    print(roc_auc_score(y,y_hat))
    pass

def SPB_Eval(test_df, predict_df):
    pass

def get_model_and_hparams(dataset):
    if dataset == 'vdjdb':
        version = '1veajht'
    if dataset == 'mcpas':
        version = '1meajht'
    # get model file from version
    checkpoint_path = os.path.join('Models', 'version_' + version, 'checkpoints')
    files = [f for f in listdir(checkpoint_path) if isfile(join(checkpoint_path, f))]
    checkpoint_path = os.path.join(checkpoint_path, files[0])
    # get args from version
    args_path = os.path.join('Models', 'version_' + version, 'meta_tags.csv')
    with open(args_path, 'r') as file:
        lines = file.readlines()
        args = {}
        for line in lines[1:]:
            key, value = line.strip().split(',')
            if key in ['dataset', 'tcr_encoding_model', 'cat_encoding']:
                args[key] = value
            else:
                args[key] = eval(value)
    hparams = Namespace(**args)
    checkpoint = checkpoint_path
    model = load_model(hparams, checkpoint)
    train_pickle = 'Samples/' + model.dataset + '_train_samples.pickle'
    test_pickle = 'Samples/' + model.dataset + '_test_samples.pickle'
    datafiles = train_pickle, test_pickle
    return model, datafiles, hparams


def IdoAuc(dataset):
    model, datafiles, hparams = get_model_and_hparams(dataset)
    true_test = ev.efficient_true_new_pairs(hparams, datafiles)
    print('tpp i:', ev.tpp_i(model, datafiles, true_test))
    print('tpp ii:', ev.tpp_ii(model, datafiles, true_test))
    print('tpp iii:', ev.tpp_iii(model, datafiles, true_test))



if __name__ == '__main__':
    IdoAuc("mcpas")