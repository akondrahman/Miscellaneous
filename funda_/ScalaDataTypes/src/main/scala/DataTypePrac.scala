/* Scala Data Types Practice */
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.apache.spark.mllib.linalg.{Vector, Vectors}
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.util.MLUtils
import org.apache.spark.rdd.RDD
import org.apache.spark.mllib.linalg.{Matrix, Matrices}
import org.apache.spark.mllib.linalg.distributed.RowMatrix
import org.apache.spark.mllib.linalg.distributed.{IndexedRow, IndexedRowMatrix, RowMatrix}

object DataTypePrac{
  def main(args: Array[String]){
      /* create spark conf  */
      val conf = new SparkConf().setAppName("MyFirstApplication")
      /* create spark context */
      val sc = new SparkContext(conf)
      /*basic data types*/
      val denseVec:   Vector = Vectors.dense(1.0, 0.0, 3.0)
      val sparseVec1: Vector = Vectors.sparse(3, Array(0, 9), Array(1, 101.0)) /* (index, value) : syntax of Array */
      val sparseVec2: Vector = Vectors.sparse(3, Seq((0, 50.0), (2, 99.0)))  /* (index, value) : syntax of sequence */

      /* labeled points: meeded for classification, one label, accompnaied by a few datasets*/
      val defectedData    = LabeledPoint(1.0, Vectors.dense(1.0, 1.0, 2.5))
      val nonDefectedData = LabeledPoint(0.0, Vectors.dense(5.0, 6.5, 7.5))
      println("Sparse (vector 2) data sample")
      for ( index <- 0 to (sparseVec2.size - 1)) {
         println(sparseVec2(index))
      }
      val sampleMLDataFile = "/usr/local/Cellar/apache-spark/1.6.1/libexec/data/mllib/sample_libsvm_data.txt"
      val sampleData: RDD[LabeledPoint] = MLUtils.loadLibSVMFile(sc, sampleMLDataFile)
      println("Read from file ...")
      println(sampleData.toString())

      /*Dense matrix practice*/
      val myDenseMatrix: Matrix = Matrices.dense(3, 3, Array(99.0, 1.0, 0.0, 3.5, 99.0, 75.1, 0.0, 51.5, 99.0))
      /* Distributed Matrix Practice */
      val vector1 = Vectors.dense(1.0, 0.0, 3.0)
      val vector2 = Vectors.sparse(3, Array(1), Array(2.5))
      val vector3 = Vectors.sparse(3, Seq((0, 1.5), (1, 1.8)))
      val vector_parallel= sc.parallelize(Seq(vector1, vector2, vector3))
      val myRowMat: RowMatrix = new RowMatrix(vector_parallel) 
      val distMatRow = myRowMat.numRows()
      val distMatCol = myRowMat.numCols()
      println(s"Count of rows (distributed matrix): $distMatRow, and count of columns: $distMatCol")         
      println("=============================================")
      val indexedRows: RDD[IndexedRow]  = sc.parallelize(Array(IndexedRow(2, Vectors.dense(1, 3)), IndexedRow(4, Vectors.dense(4, 5)))) // an RDD of indexed row
      val indexedMat:  IndexedRowMatrix = new IndexedRowMatrix(indexedRows)
      val indiMatRow = indexedMat.numRows()
      val indiMatCol = indexedMat.numCols()      
      println(s"Count of rows (indexed matrix): $indiMatRow, and count of columns: $indiMatCol")         
      println("=============================================")      
  }
}  