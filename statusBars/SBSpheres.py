class SBSpheres():

    ## Initialize
    #   Init setsup the positional argumnts of the sphere based UI
    def __init__(self, ypos, offset, amount, width, height, canvas):
        self.ypos = ypos
        self.offset = offset
        self.amount = amount
        self.width = width
        self.height = height
        self.canvas = canvas

    def update(self, state):
        # Prevent overcompletion
        if state > 100:
            state = 100

        #Calculate sizes
        #border  = self.width - (self.offset *2)
        size    = ( self.width - ((self.amount + 1) * self.offset) ) / self.amount

        # Initialize bar segments
        segment_size    = ( 100 / self.amount )

        # Loop Through  all spheres
        for segment in range( 0, self.amount ):

            # Calculate sphere completion
            segment_state   = 0
            if state <= ( segment_size * segment ):
                segment_state = 0
            elif ( state >= ( segment_size * segment ) ) and ( state <= ( segment_size * ( segment + 1 ) ) ):
                segment_state = 100 * ( ( state - ( segment_size * segment )) / float( segment_size ) )
            else:
                segment_state = 100
            self.drawBall((self.offset + ( size / 2 ) + ( (size + self.offset ) * segment) ), self.ypos, size, segment_state)

    ## drawBall
    #  Draws spheres to screen with a default fill of 100
    def drawBall( self, x, y, size, fill=100 ):
        radius = size / 2
        filler = radius * float( fill / 100.0 )

        # Underlaying Coordinates
        xposTop     = x + ( radius )
        yposTop     = y + ( radius )
        xposBottom  = x - ( radius )
        yposBottom  = y - ( radius )

        # Underlaying oval
        self.canvas.create_oval(xposTop, yposTop, xposBottom, yposBottom, fill="grey", stipple='gray75', outline="black", width=2)

        # Filler Coordinates
        xposTop     = x + ( filler )
        yposTop     = y + ( filler )
        xposBottom  = x - ( filler )
        yposBottom  = y - ( filler )

        # Sphere filler
        self.canvas.create_oval(xposTop, yposTop, xposBottom, yposBottom, fill="#1adb37", outline="")
