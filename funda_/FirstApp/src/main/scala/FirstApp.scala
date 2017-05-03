/* My First Scala Application */

import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf 


object FirstApp{
  def main(args: Array[String]){
  	  /* set the file name */
      val fileToRead = "/Users/akond/Documents/AkondOneDrive/OneDrive/IaC-Tree/dataset/Mozilla.Final.Categ.csv"
  	  /* create spark conf  */
      val conf = new SparkConf().setAppName("MyFirstApplication")
  	  /* create spark context */
      val sc = new SparkContext(conf)
      /* read the file using textFile(), then cache it using cache() */
      val dataFromFile = sc.textFile(fileToRead, 2).cache()
      /*apply filter to find out which line contains the word 'file', using filter(), line=>, and line.contains()*/
      val cntOfFiles = dataFromFile.filter(line => line.contains("file")).count()
      val cntOfAkonds = dataFromFile.filter(line => line.contains("akond")).count() 
      /* print to console */
      println(s"Count of lines with 'file': $cntOfFiles, and count of lines with 'akond': $cntOfAkonds")
      sc.stop()     
  }	
}