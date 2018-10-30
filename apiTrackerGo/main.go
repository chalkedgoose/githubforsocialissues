package main

import (
	"fmt"
	"context"
	"log"
	"github.com/mongodb/mongo-go-driver/mongo"
)

// MONGOURI: mongodb://localhost:27017/githubforsocialissues

func main() {

	client, err := mongo.NewClient("mongodb://localhost:27017")
	if err != nil {
		log.Fatal(err)
	}
	err = client.Connect(context.TODO())
	if err != nil {
		log.Fatal(err)
	}
	// The Reqs connection from the MongoDatabase
	collection := client.Database("githubforsocialissues").Collection("reqs")
	
	


	fmt.Println(collection)


}
