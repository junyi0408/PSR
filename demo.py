import open3d as o3d
from poisson_reconstruct import psr

if __name__ == "__main__":
    # read point cloud
    pcd = o3d.io.read_point_cloud("data\Armadillo_sampled.pcd")

    # PSR
    psr(pcd)

    # visualize result
    o3d.visualization.draw([pcd])