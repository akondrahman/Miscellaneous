/* Stat using MLLib */
import org.apache.spark.mllib.linalg.{Vector, Vectors}
import org.apache.spark.mllib.linalg.Vector
import org.apache.spark.mllib.stat.{MultivariateStatisticalSummary, Statistics}
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.apache.spark.mllib.linalg.{Matrix, Matrices}
import org.apache.spark.mllib.stat.Statistics
import org.apache.spark.rdd.RDD
import org.apache.spark.mllib.stat.KernelDensity



object StatPrac{
	def main(args: Array[String]){
      /* create spark conf  */
      val conf = new SparkConf().setAppName("SparkStatApplication")
      /* create spark context */
      val sc = new SparkContext(conf)
      /* ceate the RDD of Vectors: one vector is X, and the other is Y*/
      val rddVecs = sc.parallelize(List(Vectors.dense(12, 10996), Vectors.dense(1, 996), Vectors.dense(31, 106), Vectors.dense(35, 6718), Vectors.dense(78, 996)))
      val stat_summary: MultivariateStatisticalSummary = Statistics.colStats(rddVecs)
      println("===================================")
      println(stat_summary.mean) //mean value for each column 
      println(stat_summary.variance) // variance for each column 
      println("===================================")    
      val corrMat: Matrix  = Statistics.corr(rddVecs, "spearman")       	
      println(corrMat.toString)
      println("===================================")    
      val data = sc.parallelize(Seq((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')))
      val fractions = Map(1 -> 0.1, 2 -> 0.6, 3 -> 0.3) /*specfy, what fraction do you need */
      /* get an approximate sample */
      val apprSample = data.sampleByKey(withReplacement = false, fractions = fractions)
      /* get an exact sample */
      val exactSample = data.sampleByKeyExact(withReplacement = false, fractions = fractions)
      println(apprSample.toString)
      println(exactSample.toString)      
      println("===================================") 
      val control_data: RDD[Double] = sc.parallelize(Seq(0.11, 0.27, 0.39, 0.01, 0.45, 0.76))
      val treatme_data: RDD[Double] = sc.parallelize(Seq(0.19, 0.57, 0.99, 0.17, 0.95, 0.36))      
      //val testRes = Statistics.kolmogorovSmirnovTest(control_data, treatme_data)
      //println(testRes)
      val kd_control = new KernelDensity().setSample(control_data).setBandwidth(3.0)
      println(kd_control)
      println("===================================")       
	}
}