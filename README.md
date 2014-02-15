Post Acitivity by Date for Forum Data
==============================

Basic MapReduce Hadoop Streaming Python scripts to measure post activity in forum data by date.

This MapReduce script creates a tab separated file with two columns, date %Y-%m-%d \t number of posts.

For demonstration purposes, it assumed that the input posts text file (forum_node.tsv) is a tab separated file with the following columns:

* "id": id of the node
* "title": title of the node. in case "node_type" is "answer" or "comment", this field will be empty
* "tagnames": space separated list of tags
* "author_id": id of the author
* "body": content of the post
* "node_type": type of the node, either "question", "answer" or "comment"
* "parent_id": node under which the post is located, will be empty for "questions"
* "abs_parent_id": top node where the post is located
* "added_at": date added
* plus an additional ten columns of data

### Usage
You can simulate the execution using shell pipes
```shell
cat forum_node.tsv | ./mapper.py | sort | ./reducer.py > posts_by_date.tsv
```  

To run this in a hadoop environment, first set up the alias in the .bashrc
```shell
run_mapreduce() {
        hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper $1 -reducer $2 -file $1 -file $2 -input $3 -output $4
}

run_mapreduce_with_combiner() {
        hadoop jar /usr/lib/hadoop-0.20-mapreduce/contrib/streaming/hadoop-streaming-2.0.0-mr1-cdh4.1.1.jar -mapper $1 -reducer $2 -combiner $2 -file $1 -file $2 -input $3 -output $4
}


alias hs=run_mapreduce

alias hsc=run_mapreduce_with_combiner
```

Once the alias has been setup you can either run the process as a MapReduce or as a MapReduce using reduce.py as both the reducer and combiner for improved distributed performance.

eg.

```shell
hs mapper.py reducer.py forum_data posts_by_date
```
Or with a combiner
```shell
hsc mapper.py reducer.py forum_data posts_by_date
```

where:
* "forum_data" is the folder in the HDFS containing the forum node text records
* "inverted_index" is the output data folder, it is important that this folder doesn't already exist.

### Output

The reducer generates a text stream with a tab separated index containing the date followed by the sum total for post for that date.
 

```
%Y-%m-%d \t total_posts  
```
