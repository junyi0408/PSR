import open3d as o3d
import numpy as np

def psr(
    pcd : o3d.geometry.PointCloud,
    depth = 8
    )-> o3d.geometry.TriangleMesh:
    # obtain the normals
    pcd.estimate_normals()
    pcd.orient_normals_consistent_tangent_plane(30)

    # set up the octree
    octree = o3d.geometry.Octree(depth)
    octree.convert_from_point_cloud(pcd)
    
    

    return