import os
import json
from nclt2rosbag.definitions import ROOT_DIR


class BaseRawData:
    """Base class to initialize the directories for the raw data

    USAGE:
            BaseRawData('2013-01-10')

    """
    def __init__(self, date):

        # init date
        if isinstance(date, str):
            self.date = date
        else:
            raise TypeError('"date" must be of type string')

        # init raw directory
        self.raw_data_dir = ROOT_DIR + '/raw_data/' + str(self.date)

        # check if data exists
        if os.path.exists(self.raw_data_dir):

            self.ground_truth_dir = self.raw_data_dir + '/ground_truth'
            if os.path.exists(self.ground_truth_dir):
                self.ground_truth_flag = True
            else:
                self.ground_truth_flag = False

            self.ground_truth_covariance_dir = self.raw_data_dir + '/ground_truth_covariance'
            if os.path.exists(self.ground_truth_covariance_dir):
                self.ground_truth_covariance_flag = True
            else:
                self.ground_truth_covariance_flag = False

            self.hokuyo_data_dir = self.raw_data_dir + '/hokuyo_data'
            if os.path.exists(self.hokuyo_data_dir):
                self.hokuyo_data_flag = True
            else:
                self.hokuyo_data_flag = False

            self.sensor_data_dir = self.raw_data_dir + '/sensor_data'
            if os.path.exists(self.sensor_data_dir):
                self.sensor_data_flag = True
            else:
                self.sensor_data_flag = False

            self.velodyne_data_dir = self.raw_data_dir + '/velodyne_data'
            if os.path.exists(self.velodyne_data_dir):
                self.velodyne_data_flag = True
                self.velodyne_sync_data_dir = self.raw_data_dir + '/velodyne_data/' + '%s' % self.date + '/velodyne_sync/'
            else:
                self.velodyne_data_flag = False

            self.images_dir = self.raw_data_dir + '/images'
            if os.path.exists(self.images_dir):
                self.images_flag = True
                self.images_lb3_dir = self.raw_data_dir + '/images/' + '%s' % self.date + '/lb3/'
            else:
                self.images_flag = False

        else:
            raise ValueError("raw_data directory not exists")

        # open json configuration file
        with open(ROOT_DIR + '/cfg/configuration.json') as json_configs:
            self.json_configs = json.load(json_configs)

        # create rosbag directory
        self.rosbag_dir = ROOT_DIR + '/rosbags/%s' % self.date
        if not os.path.exists(self.rosbag_dir):
            os.makedirs(self.rosbag_dir)

        # create camera folder settings
        self.num_cameras = 6