package configs

import (
	"github.com/spf13/viper"
)

var cfg *Config

type Config struct {
	API APIConfig
	DB  DBConfig
}
type APIConfig struct {
	Port string
}

type DBConfig struct {
	Host     string
	Port     string
	User     string
	Pass     string
	Database string
}

func init() {
	viper.SetDefault("api.port", "9000")
	viper.SetDefault("data.host", "localhost")
	viper.SetDefault("data.port", "5432")
}

func Load() error {
	viper.SetConfigName("config")
	viper.SetConfigType("toml")
	viper.AddConfigPath(".")
	err := viper.ReadInConfig()
	if err != nil {
		if _, ok := err.(viper.ConfigFileNotFoundError); !ok {
			return err
		}
	}

	cfg = new(Config)

	cfg.API = APIConfig{
		Port: viper.GetString("api.port"),
	}

	cfg.DB = DBConfig{
		Host:     viper.GetString("data.host"),
		Port:     viper.GetString("data.port"),
		User:     viper.GetString("data.user"),
		Pass:     viper.GetString("data.pass"),
		Database: viper.GetString("data.name"),
	}

	return nil
}

func GetDB() DBConfig {
	return cfg.DB
}

func GetServerPort() string {
	return cfg.API.Port
}
