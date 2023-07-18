package db

import (
	"database/sql"
	"fmt"

	"github.com/geavenx/api-postgres/configs"
	_ "github.com/lib/pq"
)

func OpenConnection() (*sql.DB, error) {
	conf := configs.GetDB()
	sslmode := "disable"
	sc := fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=%s",
		conf.Host, conf.Port, conf.User, conf.Pass, conf.Database, sslmode)

	conn, err := sql.Open("postgres", sc)
	if err != nil {
		panic(err)
	}

	err = conn.Ping()

	return conn, err
}
