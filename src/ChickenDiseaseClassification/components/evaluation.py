import tensorflow as tf
from pathlib import Path
from urllib.parse import urlparse
import mlflow
import mlflow.tensorflow
from ChickenDiseaseClassification.entity.config_entity import EvaluationConfig
from ChickenDiseaseClassification.utils.common import save_json
model = tf.keras.models.load_model("artifacts/training/model.h5")


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config


    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        self.tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        with mlflow.start_run():
            self.log_into_mlflow()
            self.model = self.load_model(self.config.path_of_model)
            self._valid_generator()
            self.score = self.model.evaluate(self.valid_generator)


            mlflow.log_params(self.config.all_params)


            
            mlflow.log_metrics({"loss": self.score[0], "accuracy": self.score[1]})
            


            # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # please refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                

            # Log metrics
            if self.tracking_url_type_store != "file":

                # Register the model
                
                mlflow.sklearn.log_model(model, "model", registered_model_name="ChickenDisease")
            else:
                mlflow.sklearn.log_model(model, "model")


    
    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    