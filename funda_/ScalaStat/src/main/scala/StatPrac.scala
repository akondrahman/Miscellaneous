/* Stat using MLLib */

import org.apache.spark.mllib.linalg.Vector
import org.apache.spark.mllib.stat.{MultivariateStatisticalSummary, Statistics}

object StatPrac{
	def main(args: Array[String]){
      /* create spark conf  */
      val conf = new SparkConf().setAppName("StatApplication")
      /* create spark context */
      val sc = new SparkContext(conf)
      /* ceate the RDD of Vectors: one vector is X, and the other is Y*/
      val rddVecs = sc.parallelize(List(Vectors.dense(12, 10996), Vectors.dense(1, 996), Vectors.dense(31, 106), Vectors.dense(35, 6718), Vectors.dense(78, 996)))
      val stat_summary: MultivariateStatisticalSummary = Statistics.colStats(rddVecs)
      println("===================================")
      println(stat_summary.mean) //mean value for each column 
      println(stat_summary.variance) // variance for each column 
      println("===================================")           	
	}
}