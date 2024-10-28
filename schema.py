from graphene import ObjectType, Float, Field, List, Schema, Boolean, String    
from graphene.types.generic import GenericScalar
from geometry import (
    calculate_bounding_box, rotate_mesh, move_mesh, is_polygon_convex
)

class BoundingBox(ObjectType):
    minPoint = GenericScalar()
    maxPoint = GenericScalar()

class Query(ObjectType):
    bounding_box = Field(BoundingBox, points=List(GenericScalar, required=True))
    rotated_mesh = List(GenericScalar, mesh=List(GenericScalar), angle=Float(), axis=String())
    moved_mesh = List(GenericScalar, mesh=List(GenericScalar), x=Float(), y=Float(), z=Float())
    is_convex = Boolean(points=List(GenericScalar))

    def resolve_bounding_box(self, info, points):
        return calculate_bounding_box(points)

    def resolve_rotated_mesh(self, info, mesh, angle, axis):
        return rotate_mesh(mesh, angle, axis)

    def resolve_moved_mesh(self, info, mesh, x, y, z):
        return move_mesh(mesh, x, y, z)

    def resolve_is_convex(self, info, points):
        return is_polygon_convex(points)

schema = Schema(query=Query)

