/* Scala Data Types Practice */
import org.apache.spark.mllib.linalg.{Vector, Vectors}
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.util.MLUtils
import org.apache.spark.rdd.RDD


object DataTypePrac{
  def main(args: Array[String]){
      /* create spark conf  */
      val conf = new SparkConf().setAppName("MyFirstApplication")
      /* create spark context */
      val sc = new SparkContext(conf)
      /*basic data types*/
      val denseVec:   Vector = Vectors.dense(1.0, 0.0, 3.0)
      val sparseVec1: Vector = Vectors.sparse(3, Array(1, 9), 99.0)
      val sparseVec2: Vector = Vectors.sparse(Seq((40.0, 50.0), (11.0, 99.0)), 5.0)

      /* labeled points: meeded for classification, one label, accompnaied by a few datasets*/
      val defectedData    = LabeledPoint(1.0, Vectors.dense(1.0, 1.0, 2.5))
      val nonDefectedData = LabeledPoint(0.0, Vectors.dense(5.0, 6.5, 7.5))

      val sampleMLDataFile = "/usr/local/Cellar/apache-spark/1.6.1/libexec/data/mllib/sample_libsvm_data.txt"
      val sampleData: RDD[LabeledPoint] = MLUtils.loadLibSVMFile(sc, sampleMLDataFile)
  }
}  