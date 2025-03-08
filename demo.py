from housing.pipeline.pipeline import Pipeline
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation
import os


def main():
    try:
        # +++++++++get_model_pusher_config() Check++++++++++
        # model_pusher_config = Configuration().get_model_pusher_config()
        # print(model_pusher_config)
        # +++++++++get_model_trainer_config() Done++++++++++


        # +++++++++get_model_evaluation_config() Check++++++++++
        #  model_evaluation_config = Configuration().get_model_evaluation_config()
        #  print(model_evaluation_config)
        # +++++++++get_model_trainer_config() Done++++++++++


        # +++++++++get_model_trainer_config() Check++++++++++
        # model_traine_config = Configuration().get_model_trainer_config()
        # print(model_traine_config)
        # +++++++++get_model_trainer_config() Done++++++++++

        # +++++++++get_data_transformation_config() Check++++++++++
        # data_transformation_config = Configuration().get_data_transformation_config()
        # print(data_transformation_config)
        # +++++++++get_data_transformation_config() Done++++++++++

        # +++++++++get_data_validation_config() Check++++++++++
        # data_validation_config = Configuration().get_data_validation_config()
        # print(data_validation_config)
        # +++++++++get_data_validation_config() Done++++++++++

        # +++++++++get_data_ingestion_config() Check++++++++++
        #data_ingestion_config = Configuration().get_data_ingestion_config()
        #print(data_ingestion_config)
        # +++++++++get_data_ingestion_config() Done++++++++++



        # file_path =r"D:\ML\MLOps_house_price_project\config\schema.yaml"
        # schema_file_path =r"D:\ML\MLOps_house_price_project\housing\artifact\data_ingestion\2025-02-24-01-13-00\ingested_data\train\housing.csv"  
        # df = DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path
        # )
        # print(df.columns)
        # print(df.dtypes)
        

        # +++++++++ CHECK ANY COMPONENT ++++++++++
        # config_file_path="D:\ML\MLOps_house_price_project\config\config.yaml"
        # pipeline = Pipeline(config=Configuration(config_file_path=config_file_path))
        # pipeline.run_pipeline()

        # +++++++++CHECK ANY COMPONENT DONE++++++++++


        # +++++++++RUN PIPELINE THREAD CLASS+++++++++
        # config_file_path="D:\ML\MLOps_house_price_project\config\config.yaml"

        config_path =  os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuration(config_file_path=config_path))
        # pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed")

        # +++++++++RUN PIPELINE THREAD CLASS DONE+++++++++

    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__=="__main__":
    main()